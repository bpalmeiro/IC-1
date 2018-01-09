
.. _my-label-EventModel:

Event Model 
------------------

To be updated.

.. graphviz::

   digraph hierarchy {
   size="20,20"
   node[shape=record,style=filled,fillcolor=gray95]
   edge[dir=back, arrowtail=empty]



   2[label = "{Event|event_no\ltimestamp\lrun_number?\l}"]
   3[label = "{Track Collection|tracks|store()}"]
   4[label = "{Hit Collection|hits|store()}"]
   5[label = "{Kr Event|S1,S2,...|store()}"]


   2->3
   2->4
   2->5
   3->113[constraint=false, arrowtail=odiamond]
   4->15[constraint=false, arrowtail=odiamond]


   112[label = "{Voxel Collection|voxels:[V]\lE}"]
   113[label = "{Track|blobs:[B]\lextrema:[V]}"]
   114[label = "{Blob |seed: x,y,z\lsize:polymorphic}"]

   112->113
   112->114
   113->114[constraint=false, arrowtail=odiamond]
   112->14[constraint=false, arrowtail=odiamond]
   113->1112[constraint=false, arrowtail=odiamond]
   
   12[label = "{xyzE|x,y,z,E}"]
   13[label = "{MCHit|t}"]
   14[label = "{SpaceElement|size\l[hitE]\l}"]
   15[label = "{Hit|cluster\lpeaks_no\l}"]
   16[label = "{Cluster|Q\lxy\lxy_var\ln_sipm\l}"]


   12->13
   12->14
   12->15
   15->16[constraint=false, arrowtail=odiamond]

   1112[label = "{Voxel}"]
   1113[label = "{Sphere}"]
   1114[label = "{etc...}"]

   14->1112
   14->1113
   14->1114
   

   }
