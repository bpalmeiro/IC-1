

Define overall structure here
Keep same style for all sections.
This is a test ``invisible_cities/whatever/stuff.py``.


Cities
------------------

Isidora
+++++


.. graphviz::

   digraph G {bgcolor=skyblue label="ISIDORA\n" labelloc=top fontsize=16 size=6

   node [style=filled,color=white] read_wf, correct_pmt, write_wf;
   PMT_RWF_in  [shape=box,     label="PMT RWF", fontsize=13, width=0.1]
   PMT_CWF_out [shape=invhouse,label="PMT CWF", fontsize=13, width=0.1]
   read_wf     [fontcolor=red, fontname=Courier];
   correct_pmt [fontcolor=red, fontname=Courier];
   write_wf    [fontcolor=red, fontname=Courier];

   PMT_RWF_in  -> read_wf;
   read_wf     -> correct_pmt [ label = " RWF", fontname=Courier];
   correct_pmt -> write_wf    [ label = " RWF", fontname=Courier ];
   write_wf    -> PMT_CWF_out;

   SiPM_RWF_in  [shape=box,  label="SiPM RWF", fontsize=13, width=0.1]
   SiPM_RWF_out [shape=invhouse, label="SiPM RWF", fontsize=13, width=0.1]
   SiPM_RWF_in -> SiPM_RWF_out;


   MC_Track_in  [shape=box,  label="MC Track", fontsize=13, width=0.1]
   MC_Track_out [shape=invhouse, label="MC Track", fontsize=13, width=0.1]
   MC_Track_in -> MC_Track_out;

   Run_info_in  [shape=box,  label="Run Info", fontsize=13, width=0.1]
   Run_info_out [shape=invhouse, label="Run Info", fontsize=13, width=0.1]
   Run_info_in -> Run_info_out;

   {rank = same; PMT_RWF_in; SiPM_RWF_in; MC_Track_in; Run_info_in;}
   {rank = same; SiPM_RWF_out; PMT_CWF_out; MC_Track_out; Run_info_out;}
   }


Example of adding code::
  some code here

  
  

Irene
+++++

   
.. graphviz::

   digraph G {bgcolor=skyblue label="IRENE\n" labelloc=top fontsize=16 size=6

   node [style=filled,color=white];
   PMT_RWF_in  [shape=box,      label="PMT RWF", fontsize=13, width=0.1]
   PMAPS       [shape=invhouse, label="PMAPS",   fontsize=13, width=0.1]
   read_wf_pmt         [fontcolor=red, fontname=Courier];
   correct_pmt         [fontcolor=red, fontname=Courier];
   sum_calibrated_pmt  [fontcolor=red, fontname=Courier];
   zero_suppress_PMT   [fontcolor=red, fontname=Courier];
   find_s1s2           [fontcolor=red, fontname=Courier];
   write_pmaps         [fontcolor=red, fontname=Courier];

   PMT_RWF_in          -> read_wf_pmt;
   read_wf_pmt         -> correct_pmt        [ label = " RWF",    fontname=Courier];
   correct_pmt         -> sum_calibrated_pmt [ label = " RWF",    fontname=Courier];
   sum_calibrated_pmt  -> zero_suppress_PMT  [ label = " PMTSUM", fontname=Courier];
   zero_suppress_PMT   -> find_s1s2          [ label = " PMTSUM", fontname=Courier];
   find_s1s2           -> compute_s2si_S2Si  [ label = " S1S2",   fontname=Courier];
   write_pmaps         -> PMAPS;         

   SiPM_RWF_in        [shape=box,  label="SiPM RWF", fontsize=13, width=0.1]
   read_wf_sipm       [fontcolor=red, fontname=Courier];
   calibrate_sipm     [fontcolor=red, fontname=Courier];
   zero_suppress_SIPM [fontcolor=red, fontname=Courier];
   compute_s2si_S2Si  [fontcolor=red, fontname=Courier];
   
   SiPM_RWF_in         -> read_wf_sipm;
   read_wf_sipm        -> calibrate_sipm     [ label = " RWF",    fontname=Courier];
   calibrate_sipm      -> zero_suppress_SIPM [ label = " RWF",    fontname=Courier];
   zero_suppress_SIPM  -> compute_s2si_S2Si  [ label = " RWF",    fontname=Courier];
   compute_s2si_S2Si   -> write_pmaps        [ label = " PMAPS",   fontname=Courier];

   MC_Track_in  [shape=box,  label="MC Track", fontsize=13, width=0.1]
   MC_Track_out [shape=invhouse, label="MC Track", fontsize=13, width=0.1]
   MC_Track_in -> MC_Track_out;

   Run_info_in  [shape=box,  label="Run Info", fontsize=13, width=0.1]
   Run_info_out [shape=invhouse, label="Run Info", fontsize=13, width=0.1]
   Run_info_in -> Run_info_out;

   {rank = same; PMT_RWF_in; SiPM_RWF_in; MC_Track_in; Run_info_in;}
   {rank = same; MC_Track_out; Run_info_out; PMAPS;}
   {rank = same; sum_calibrated_pmt; calibrate_sipm;}
   {rank = same; zero_suppress_PMT; zero_suppress_SIPM;}
   {rank = same; read_wf_pmt; read_wf_sipm;}
   }

Dorotea
+++++

`This is a Notebook Example <https://github.com/bpalmeiro/ICARO/blob/Michel/icaro/KrMay/Run4670.ipynb/>`_

.. graphviz::

   digraph G {bgcolor=skyblue label="DOROTEA\n" labelloc=top fontsize=16 size=6

   node [style=filled,color=white]

   PMAPS     [shape=box, label="PMAPS", fontsize=13, width=0.1]
   KDST      [shape=invhouse,label="KDST", fontsize=13,width=0.1]
   read_pmaps   [fontcolor=red, fontname=Courier];
   filter_1s1   [fontcolor=red, fontname=Courier];
   write_kdst   [fontcolor=red, fontname=Courier];
   compute_kdst [fontcolor=red, fontname=Courier];

   PMAPS        -> read_pmaps;
   read_pmaps   -> filter_1s1   [ label = " PMAPS", fontname=Courier];
   filter_1s1   -> compute_kdst [ label = " PMAPS", fontname=Courier ];
   compute_kdst -> write_kdst   [ label = " KDST", fontname=Courier ];
   write_kdst   -> KDST;

   Run_info_in  [shape=box,  label="Run Info", fontsize=13, width=0.1]
   read_run_info[fontcolor=red, fontname=Courier];
   Run_info_in   -> read_run_info;
   read_run_info -> compute_kdst [ label = " RUN INFO", fontname=Courier];

   MC_Track_in  [shape=box,  label="MC Track", fontsize=13, width=0.1]
   MC_Track_out [shape=invhouse, label="MC Track", fontsize=13, width=0.1]
   MC_Track_in -> MC_Track_out;


   {rank = same; PMAPS; Run_info_in; MC_Track_in}
   {rank = same; KDST; MC_Track_out;}
   }



Penthesilea
+++++++++++


.. graphviz::

   digraph G {bgcolor=skyblue label="PENTHESILEA\n" labelloc=top fontsize=16 size=6

   node [style=filled,color=white]

   PMAPS_in     [shape=box, label="PMAPS", fontsize=13, width=0.1]
   PMAPS_out    [shape=invhouse,label="PMAPS", fontsize=13,width=0.1]
   TRACKS       [shape=invhouse,label="TRACKS", fontsize=13,width=0.1]
   read_pmaps   [fontcolor=red, fontname=Courier];
   filter       [fontcolor=red, fontname=Courier];
   compute_hits [fontcolor=red, fontname=Courier];
   paolina      [fontcolor=red, fontname=Courier];
   write_tracks [fontcolor=red, fontname=Courier];
   write_pmaps  [fontcolor=red, fontname=Courier];

   PMAPS_in     -> read_pmaps;
   read_pmaps   -> filter       [ label = " PMAPS",  fontname=Courier];
   filter       -> compute_hits [ label = " PMAPS",  fontname=Courier ];
   compute_hits -> paolina      [ label = " HITS",   fontname=Courier ];
   paolina      -> write_tracks [ label = " TRACKS", fontname=Courier ];
   write_tracks -> TRACKS;
   filter       -> write_pmaps  [ label = " PMAPS",  fontname=Courier ];
   write_pmaps  -> PMAPS_out;
   
   MC_Track_in  [shape=box,  label="MC Track", fontsize=13, width=0.1]
   MC_Track_out [shape=invhouse, label="MC Track", fontsize=13, width=0.1]
   MC_Track_in -> MC_Track_out;

   Run_info_in  [shape=box,  label="Run Info", fontsize=13, width=0.1]
   Run_info_out [shape=invhouse, label="Run Info", fontsize=13, width=0.1]
   Run_info_in -> Run_info_out;

   {rank = same; write_tracks; write_pmaps;}
   {rank = same; PMAPS_in;  Run_info_in; MC_Track_in;}
   {rank = same; PMAPS_out; TRACKS; MC_Track_out; Run_info_out;}
   }


Zaira
+++++++++++


.. graphviz::

   digraph G {bgcolor=skyblue label="ZAIRA\n" labelloc=top fontsize=16 size=6

   node [style=filled,color=white]

   KDST               [shape=box, label="KDST", fontsize=13, width=0.1]
   CORRECTION_MATRIX  [shape=invhouse,label="CORRECTION_MATRIX", fontsize=13,width=0.1]
   read_kdst                [fontcolor=red, fontname=Courier];
   filter                   [fontcolor=red, fontname=Courier];
   compute_correction_table [fontcolor=red, fontname=Courier];
   write_correction_matrix  [fontcolor=red, fontname=Courier];

   KDST         -> read_kdst;
   read_kdst    -> filter                   [ label = " KDST",  fontname=Courier];
   filter       -> compute_correction_table [ label = " KDST",  fontname=Courier ];
   compute_correction_table  -> write_correction_matrix  [ label = " CORRECTION_MATRIX",  fontname=Courier ];
   write_correction_matrix   -> CORRECTION_MATRIX;
      
   }

Cecilia
+++++++
  
.. graphviz::

   digraph G {bgcolor=skyblue label="CECILIA\n" labelloc=top fontsize=16 size=6

   node [style=filled,color=white] read_wf, correct_pmt, write_wf;

   TRIGGER_PARAMS           [shape=box,     label="TRIGGER_PARAMS", fontsize=13, width=0.1]
   TRIGGER                  [shape=invhouse,label="TRIGGER", fontsize=13,width=0.1]
   PMT_RWF_in               [shape=box,     label="PMT RWF", fontsize=13, width=0.1]
   PMT_RWF_out              [shape=invhouse,label="PMT RWF", fontsize=13,width=0.1]
   read_wf                  [fontcolor=red, fontname=Courier];
   correct_pmt              [fontcolor=red, fontname=Courier];
   find_peaks               [fontcolor=red, fontname=Courier];
   trigger_emulation_filter [fontcolor=red, fontname=Courier];
   write_wf                 [fontcolor=red, fontname=Courier];

   PMT_RWF_in -> read_wf;
   read_wf                  -> correct_pmt              [ label = " RWF",   fontname=Courier];
   correct_pmt              -> find_peaks               [ label = " RWF",   fontname=Courier];
   find_peaks               -> trigger_emulation_filter [ label = " PEAKS", fontname=Courier];
   trigger_emulation_filter -> write_wf                 [ label = " RWF",   fontname=Courier];
   write_wf -> PMT_RWF_out;

   TRIGGER_PARAMS -> TRIGGER;
   TRIGGER_PARAMS -> trigger_emulation_filter;
   
   
   SiPM_RWF_in  [shape=box,  label="SiPM RWF", fontsize=13, width=0.1]
   SiPM_RWF_out [shape=invhouse, label="SiPM RWF", fontsize=13, width=0.1]
   SiPM_RWF_in -> SiPM_RWF_out;


   MC_Track_in  [shape=box,  label="MC Track", fontsize=13, width=0.1]
   MC_Track_out [shape=invhouse, label="MC Track", fontsize=13, width=0.1]
   MC_Track_in -> MC_Track_out;

   Run_info_in  [shape=box,  label="Run Info", fontsize=13, width=0.1]
   Run_info_out [shape=invhouse, label="Run Info", fontsize=13, width=0.1]
   Run_info_in -> Run_info_out;

   {rank = same; TRIGGER_PARAMS; trigger_emulation_filter;}
   {rank = same; PMT_RWF_in; SiPM_RWF_in; MC_Track_in; Run_info_in;}
   {rank = same; SiPM_RWF_out; PMT_RWF_out; MC_Track_out; Run_info_out; TRIGGER;}
   }



   
   
Diomira
+++++

.. graphviz::

   digraph G {bgcolor=skyblue label="DIOMIRA\n" labelloc=top fontsize=50 size=40
   node [style=filled,color=white];
   ranksep = 2.5;
   nodesep=0.5;

   MC_PMTRD    [shape=box,     label="MC PMT RD", fontsize=40, width=4]
   PMT_CWF_out [shape=invhouse,label="PMT CWF",   fontsize=40]
   read_wf_pmt  [fontcolor=red, fontname=Courier, label="read_wf", fontsize=40];
   ideal_pmt    [fontcolor=red, fontname=Courier, fontsize=40];
   write_wf_pmt [fontcolor=red, fontname=Courier, label="write_wf", fontsize=40];
   MC_PMTRD     -> read_wf_pmt;
   read_wf_pmt  -> ideal_pmt       [ label = " RWF", fontname=Courier,fontsize=40];
   ideal_pmt    -> write_wf_pmt    [ label = " RWF", fontname=Courier, fontsize=40];
   write_wf_pmt -> PMT_CWF_out;

   PMT_RWF_out [shape=invhouse,label="PMT RWF", fontsize=40,width=0.1]
   simulate_pmt[fontcolor=red,  fontname=Courier, fontsize=40];
   write_wf_pmt2[fontcolor=red, fontname=Courier, label="write_wf", fontsize=40];
   read_wf_pmt  -> simulate_pmt     [ label = " RWF", fontname=Courier, fontsize=40];
   simulate_pmt -> write_wf_pmt2    [ label = " RWF", fontname=Courier, fontsize=40 ];
   write_wf_pmt2 -> PMT_RWF_out;
   
   MC_SiPM      [shape=box, label="MC SiPM", fontsize=40, width=0.1]
   SiPM_RWF_out [shape=invhouse,label="SiPM RWF", fontsize=40,width=0.1]
   read_wf_sipm [fontcolor=red, fontname=Courier, label="read_wf", fontsize=40];
   simulate_sipm[fontcolor=red, fontname=Courier, fontsize=40];
   write_wf_sipm[fontcolor=red, fontname=Courier, label="write_wf", fontsize=40];
   MC_SiPM        -> read_wf_sipm;
   read_wf_sipm   -> simulate_sipm   [ label = " RWF", fontname=Courier, fontsize=40];
   simulate_sipm  -> write_wf_sipm   [ label = " RWF", fontname=Courier , fontsize=40];
   write_wf_sipm  -> SiPM_RWF_out;
   

   MC_Track_in  [shape=box,  label="MC Track", fontsize=40, width=0.1]
   MC_Track_out [shape=invhouse, label="MC Track", fontsize=40, width=0.1]
   MC_Track_in -> MC_Track_out;

   FEE_TBL_in  [shape=box,  label="FEE TBL", fontsize=40, width=0.1]
   FEE_TBL_out [shape=invhouse, label="FEE TBL", fontsize=40, width=0.1]
   FEE_TBL_in -> FEE_TBL_out;

   Run_info_in  [shape=box,  label="RUN INFO", fontsize=40, width=0.1]
   Run_info_out [shape=invhouse, label="RUN INFO", fontsize=40, width=0.1]
   get_run_and_event_info         [fontcolor=red, fontname=Courier, fontsize=40];
   gen_uniq_evt_no_from_file_hash [fontcolor=red, fontname=Courier, fontsize=40];
   run_and_event_writer           [fontcolor=red, fontname=Courier, fontsize=40];

   Run_info_in            -> get_run_and_event_info;
   get_run_and_event_info -> gen_uniq_evt_no_from_file_hash [ label = " RUN_INFO", fontname=Courier , fontsize=40];
   gen_uniq_evt_no_from_file_hash -> run_and_event_writer   [ label = " RUN_INFO", fontname=Courier , fontsize=40];
   run_and_event_writer -> Run_info_out;

   {rank = same; MC_PMTRD; MC_SiPM; MC_Track_in; FEE_TBL_in; Run_info_in}
   {rank = same; SiPM_RWF_out; PMT_CWF_out; PMT_RWF_out; MC_Track_out; FEE_TBL_out; Run_info_out}
   }


