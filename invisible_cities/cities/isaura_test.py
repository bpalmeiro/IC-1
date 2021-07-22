import os
import numpy  as np
import tables as tb

from .  isaura         import isaura
from .. core.configure import configure
from .. core.configure import all             as all_events
from .. io.dst_io      import load_dst

from .. core.testing_utils   import assert_tables_equality


def test_isaura_contains_all_tables(ICDATADIR, output_tmpdir):

    PATH_IN  = os.path.join(ICDATADIR    , "test_Xe2nu_NEW_exact_deconvolution_joint.NEWMC.h5")
    PATH_OUT = os.path.join(output_tmpdir, "contain_all_tables.isaura.h5")
    conf = configure('isaura $ICTDIR/invisible_cities/config/isaura.conf'.split())
    conf.update(dict(files_in      = PATH_IN ,
                     file_out      = PATH_OUT))
    isaura(**conf)

    tables = ["Tracking/Tracks"    ,
              "Summary/Events"     ,
              "Run/events"         , "Run/runInfo"            ,
              "MC/event_mapping"   , "MC/generators"          ,
              "MC/hits"            ,  "MC/particles"          ,
              "Filters/hits_select", "Filters/topology_select"]

    with tb.open_file(PATH_OUT, mode="r") as h5out:
        for table in tables:
            assert hasattr(h5out.root, table)



def test_isaura_empty_input_file(ICDATADIR, output_tmpdir):

    PATH_IN  = os.path.join(ICDATADIR    , "empty_file.h5")
    PATH_OUT = os.path.join(output_tmpdir, "empty_isaura.h5")
    conf = configure('isaura $ICTDIR/invisible_cities/config/isaura.conf'.split())
    conf.update(dict(files_in      = PATH_IN,
                     file_out      = PATH_OUT,
                     run_number    = 1,
                     event_range   = all_events))
    result = isaura(**conf)

    assert result.events_in   == 0
    assert result.evtnum_list == []

def test_isaura_exact(ICDATADIR, output_tmpdir):

    PATH_IN   = os.path.join(ICDATADIR    , "exact_Kr_deconvolution_with_MC.h5")
    PATH_OUT  = os.path.join(output_tmpdir, "exact_tables.isaura.h5")
    PATH_TRUE = os.path.join(ICDATADIR    , "exact_Kr_deco_tracks_with_MC.h5")
    n_evts    = 5
    conf = configure('isaura $ICTDIR/invisible_cities/config/isaura.conf'.split())
    conf.update(dict(files_in      = PATH_IN ,
                     file_out      = PATH_OUT,
                     event_range   = n_evts  ))
    np.random.seed(1234)
    isaura(**conf)

    tables = ["Tracking/Tracks"    ,
              "Summary/Events"     ,
              "Run/events"         , "Run/runInfo"            ,
              "MC/event_mapping"   , "MC/generators"          ,
              "MC/hits"            ,  "MC/particles"          ,
              "Filters/hits_select", "Filters/topology_select"]

    with tb.open_file(PATH_TRUE) as true_output_file:
        with tb.open_file(PATH_OUT) as output_file:
            for table in tables:
                obtained = getattr(     output_file.root, table)
                expected = getattr(true_output_file.root, table)
                assert_tables_equality(obtained, expected)

def test_isaura_conserves_energy(ICDATADIR, output_tmpdir):

    PATH_IN  = os.path.join(ICDATADIR    , "exact_Kr_deconvolution_with_MC.h5")
    PATH_OUT = os.path.join(output_tmpdir, "exact_tables.isaura.h5")
    n_evts = 5
    conf = configure('isaura $ICTDIR/invisible_cities/config/isaura.conf'.split())
    conf.update(dict(files_in      = PATH_IN ,
                     file_out      = PATH_OUT,
                     event_range   = n_evts  ))
    np.random.seed(1234)
    isaura(**conf)

    deco_hits   = load_dst(PATH_IN , 'DECO'    , 'Events')
    deco_tracks = load_dst(PATH_OUT, 'Tracking', 'Tracks')
    deco_events = load_dst(PATH_OUT, 'Summary' , 'Events')

    deco_hits      = deco_hits[deco_hits.event.isin(range(n_evts))]
    dhits_energy   = deco_hits  [['event', 'E'     ]].groupby(['event'])['E'     ].sum().values
    dtracks_energy = deco_tracks[['event', 'energy']].groupby(['event'])['energy'].sum().values
    devents_energy = deco_events.evt_energy.values

    np.testing.assert_allclose(dhits_energy, dtracks_energy)
    np.testing.assert_allclose(dhits_energy, devents_energy)
