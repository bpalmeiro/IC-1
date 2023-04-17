import os
import numpy  as np
import tables as tb
import pandas as pd

from pytest                    import mark
from pytest                    import raises

from .. io                     import dst_io      as dio
from .  beersheba              import beersheba
from .  beersheba              import create_deconvolution_df
from .  beersheba              import distribute_energy
from .  beersheba              import deconvolve_signal
from .. core.testing_utils     import assert_dataframes_close
from .. core.testing_utils     import assert_tables_equality
from .. database.load_db       import DataSiPM
from .. types.symbols          import HitEnergy
from .. types.symbols          import DeconvolutionMode
from .. types.symbols          import InterpolationMethod
from .. types.symbols          import CutType


def test_create_deconvolution_df(ICDATADIR):
    true_in  = os.path.join(ICDATADIR, "exact_Kr_deconvolution_with_MC.h5")
    true_dst = dio.load_dst(true_in, 'DECO', 'Events')
    ecut     = 1e-2
    new_dst  = pd.concat([create_deconvolution_df(t, t.E.values, (t.X.values, t.Y.values, t.Z.values),
                                                  CutType.abs, ecut, 3) for _, t in true_dst.groupby('event')])
    true_dst = true_dst.loc[true_dst.E > ecut, :].reset_index(drop=True)

    assert_dataframes_close(new_dst .reset_index(drop=True), true_dst.reset_index(drop=True))


@mark.parametrize("cut_type", CutType.__members__)
def test_create_deconvolution_df_cuttype(ICDATADIR, cut_type):
    true_in  = os.path.join(ICDATADIR, "exact_Kr_deconvolution_with_MC.h5")
    true_dst = dio.load_dst(true_in, 'DECO', 'Events')
    ecut     = 1e-2

    with raises(ValueError):
        create_deconvolution_df(true_dst, true_dst.E.values,
                                (true_dst.X.values, true_dst.Y.values, true_dst.Z.values),
                                cut_type, ecut, 3)


def test_distribute_energy(ICDATADIR):
    true_in   = os.path.join(ICDATADIR, "exact_Kr_deconvolution_with_MC.h5")
    true_dst1 = dio.load_dst(true_in, 'DECO', 'Events')
    true_dst2 = true_dst1[:len(true_dst1)//2].copy()
    true_dst3 = true_dst2.copy()

    distribute_energy(true_dst2, true_dst1, HitEnergy.E)

    assert np.allclose(true_dst2.E.values/true_dst2.E.sum(), true_dst3.E.values/true_dst3.E.sum())
    assert np.isclose (true_dst1.E.sum(), true_dst2.E.sum())


@mark.filterwarnings("ignore:.*not of kdst type.*:UserWarning")
def test_beersheba_contains_all_tables(deconvolution_config):
    conf, PATH_OUT = deconvolution_config
    beersheba(**conf)
    with tb.open_file(PATH_OUT) as h5out:
        assert "MC"             in h5out.root
        assert "MC/hits"        in h5out.root
        assert "MC/particles"   in h5out.root
        assert "DECO/Events"    in h5out.root
        assert "Summary/Events" in h5out.root
        assert "Run"            in h5out.root
        assert "Run/events"     in h5out.root
        assert "Run/runInfo"    in h5out.root


@mark.filterwarnings("ignore:.*not of kdst type.*:UserWarning")
def test_beersheba_exact_result_joint(ICDATADIR, deconvolution_config):
    true_out         = os.path.join(ICDATADIR, "test_Xe2nu_NEW_exact_deconvolution_joint.NEWMC.h5")
    conf, PATH_OUT   = deconvolution_config
    beersheba(**conf)

    tables = ("DECO/Events"     ,
              "Summary/Events"  ,
              "Run/events"      , "Run/runInfo"  ,
              "MC/event_mapping", "MC/generators",
              "MC/hits"         ,  "MC/particles")

    with tb.open_file(true_out)  as true_output_file:
        with tb.open_file(PATH_OUT) as      output_file:
            for table in tables:
                assert hasattr(output_file.root, table)
                got      = getattr(     output_file.root, table)
                expected = getattr(true_output_file.root, table)
                assert_tables_equality(got, expected)


@mark.filterwarnings("ignore:.*not of kdst type.*:UserWarning")
def test_beersheba_exact_result_separate(ICDATADIR, deconvolution_config):
    true_out         = os.path.join(ICDATADIR, "test_Xe2nu_NEW_exact_deconvolution_separate.NEWMC.h5")
    conf, PATH_OUT   = deconvolution_config
    conf['deconv_params']['deconv_mode'   ] = DeconvolutionMode.separate
    conf['deconv_params']['n_iterations'  ] = 50
    conf['deconv_params']['n_iterations_g'] = 50
    beersheba(**conf)

    tables = ("DECO/Events"     ,
              "Summary/Events"  ,
              "Run/events"      , "Run/runInfo"  ,
              "MC/event_mapping", "MC/generators",
              "MC/hits"         ,  "MC/particles")

    with tb.open_file(true_out)  as true_output_file:
        with tb.open_file(PATH_OUT) as      output_file:
            for table in tables:
                assert hasattr(output_file.root, table)
                got      = getattr(     output_file.root, table)
                expected = getattr(true_output_file.root, table)
                print(got)
                print(expected)
                assert_tables_equality(got, expected)


@mark.parametrize("ndim", (1, 3))
def test_beersheba_param_dim(deconvolution_config, ndim):
    conf, _ = deconvolution_config

    conf['deconv_params']['n_dim'  ] = ndim

    with raises(ValueError):
        beersheba(**conf)


@mark.parametrize("param_name", ('cut_type', 'deconv_mode', 'energy_type', 'inter_method'))
def test_deconvolve_signal_enums(deconvolution_config, param_name):
    conf, _   = deconvolution_config
    conf_dict = conf['deconv_params']

    conf_dict.pop("q_cut")
    conf_dict.pop("drop_dist")

    conf_dict[param_name] = conf_dict[param_name].name

    with raises(ValueError):
        deconvolve_signal(DataSiPM('new'), **conf_dict)


@mark.filterwarnings("ignore:.*not of kdst type.*:UserWarning")
def test_beersheba_expandvar(deconvolution_config):
    conf, _ = deconvolution_config

    conf['deconv_params']['psf_fname'] = '$ICDIR/database/test_data/PSF_dst_sum_collapsed.h5'

    beersheba(**conf)


def test_beersheba_copy_kdst(deconvolution_config, ICDATADIR):
    PATH_IN = os.path.join(ICDATADIR, "test_cdst_NEW_v1.2.0_bg.h5")
    conf, PATH_OUT = deconvolution_config
    conf["files_in"]   = PATH_IN
    conf["run_number"] = 8515

    expected_events = [3, 90, 152]

    beersheba(**conf)

    with tb.open_file(PATH_OUT) as output_file:
        assert hasattr(output_file.root, "DST/Events")

        got_events = output_file.root.DST.Events.read()["event"]
        assert expected_events == got_events.tolist()
