# Attempt at recovering the Dockerfile used to generate slaclcls/autosfx:latest:

Followed the instructions from [this image](https://hub.docker.com/r/alpine/dfimage):
```
(base) [fpoitevi@PC98123 data]$ alias dfimage="docker run -v /var/run/docker.sock:/var/run/docker.sock --rm alpine/dfimage"
(base) [fpoitevi@PC98123 data]$ dfimage -sV=1.36 slaclcls/autosfx:latest
```

Output:
```
Unable to find image 'alpine/dfimage:latest' locally
latest: Pulling from alpine/dfimage
df20fa9351a1: Pull complete 
820dbffe2156: Pull complete 
Digest: sha256:4a271e763d51b7f3cca72eac9bf508502c032665dde0e4c8d5fcf6376600f64a
Status: Downloaded newer image for alpine/dfimage:latest
latest: Pulling from slaclcls/autosfx
23884877105a: Pulling fs layer
bc38caa0f5b9: Pulling fs layer
2910811b6c42: Pulling fs layer
36505266dcc6: Pulling fs layer
d6e4a2c8a7b5: Pulling fs layer
762ec05e1176: Pulling fs layer
609bfae07d6c: Pulling fs layer
3f30cf055b23: Pulling fs layer
794509a91675: Pulling fs layer
14d0847a88f8: Pulling fs layer
c28ff9a6a62f: Pulling fs layer
c3de13afcc01: Pulling fs layer
ee3e98dd7bbe: Pulling fs layer
c4ca9355082f: Pulling fs layer
bf34076bc094: Pulling fs layer
e4c0f49642c0: Pulling fs layer
7eb94c8fa233: Pulling fs layer
dbd96ac32dbe: Pulling fs layer
778599102d38: Pulling fs layer
8786d2c46035: Pulling fs layer
c3d66bc1fe5d: Pulling fs layer
09bc74e0f4cc: Pulling fs layer
37eaecfa428c: Pulling fs layer
00381ab4380d: Pulling fs layer
9ef8c5c767b5: Pulling fs layer
e3d8190aea64: Pulling fs layer
24f12626dcfb: Pulling fs layer
1304208495f6: Pulling fs layer
a196618e031a: Pulling fs layer
699db20f1266: Pulling fs layer
771d1b87e75a: Pulling fs layer
13204b7f5a63: Pulling fs layer
a02cc6a1bbc4: Pulling fs layer
794509a91675: Waiting
14d0847a88f8: Waiting
c28ff9a6a62f: Waiting
c3de13afcc01: Waiting
ee3e98dd7bbe: Waiting
c4ca9355082f: Waiting
bf34076bc094: Waiting
e4c0f49642c0: Waiting
7eb94c8fa233: Waiting
dbd96ac32dbe: Waiting
778599102d38: Waiting
8786d2c46035: Waiting
c3d66bc1fe5d: Waiting
d6e4a2c8a7b5: Waiting
09bc74e0f4cc: Waiting
762ec05e1176: Waiting
609bfae07d6c: Waiting
37eaecfa428c: Waiting
00381ab4380d: Waiting
9ef8c5c767b5: Waiting
e3d8190aea64: Waiting
24f12626dcfb: Waiting
1304208495f6: Waiting
a196618e031a: Waiting
699db20f1266: Waiting
771d1b87e75a: Waiting
13204b7f5a63: Waiting
a02cc6a1bbc4: Waiting
3f30cf055b23: Waiting
36505266dcc6: Waiting
bc38caa0f5b9: Verifying Checksum
bc38caa0f5b9: Download complete
2910811b6c42: Verifying Checksum
2910811b6c42: Download complete
36505266dcc6: Verifying Checksum
36505266dcc6: Download complete
762ec05e1176: Verifying Checksum
762ec05e1176: Download complete
609bfae07d6c: Verifying Checksum
609bfae07d6c: Download complete
3f30cf055b23: Verifying Checksum
3f30cf055b23: Download complete
23884877105a: Verifying Checksum
23884877105a: Download complete
23884877105a: Pull complete
bc38caa0f5b9: Pull complete
2910811b6c42: Pull complete
36505266dcc6: Pull complete
794509a91675: Verifying Checksum
794509a91675: Download complete
14d0847a88f8: Download complete
c3de13afcc01: Verifying Checksum
c3de13afcc01: Download complete
ee3e98dd7bbe: Verifying Checksum
ee3e98dd7bbe: Download complete
d6e4a2c8a7b5: Verifying Checksum
d6e4a2c8a7b5: Download complete
bf34076bc094: Verifying Checksum
bf34076bc094: Download complete
d6e4a2c8a7b5: Pull complete
762ec05e1176: Pull complete
609bfae07d6c: Pull complete
3f30cf055b23: Pull complete
794509a91675: Pull complete
14d0847a88f8: Pull complete
c4ca9355082f: Verifying Checksum
c4ca9355082f: Download complete
7eb94c8fa233: Verifying Checksum
7eb94c8fa233: Download complete
c28ff9a6a62f: Verifying Checksum
c28ff9a6a62f: Download complete
dbd96ac32dbe: Verifying Checksum
dbd96ac32dbe: Download complete
778599102d38: Verifying Checksum
778599102d38: Download complete
8786d2c46035: Verifying Checksum
8786d2c46035: Download complete
c3d66bc1fe5d: Verifying Checksum
c3d66bc1fe5d: Download complete
37eaecfa428c: Download complete
00381ab4380d: Verifying Checksum
00381ab4380d: Download complete
9ef8c5c767b5: Download complete
09bc74e0f4cc: Verifying Checksum
09bc74e0f4cc: Download complete
e3d8190aea64: Verifying Checksum
e3d8190aea64: Download complete
24f12626dcfb: Download complete
c28ff9a6a62f: Pull complete
c3de13afcc01: Pull complete
ee3e98dd7bbe: Pull complete
a196618e031a: Verifying Checksum
a196618e031a: Download complete
c4ca9355082f: Pull complete
bf34076bc094: Pull complete
1304208495f6: Verifying Checksum
1304208495f6: Download complete
771d1b87e75a: Verifying Checksum
771d1b87e75a: Download complete
699db20f1266: Verifying Checksum
699db20f1266: Download complete
13204b7f5a63: Verifying Checksum
13204b7f5a63: Download complete
a02cc6a1bbc4: Verifying Checksum
a02cc6a1bbc4: Download complete
e4c0f49642c0: Verifying Checksum
e4c0f49642c0: Download complete
e4c0f49642c0: Pull complete
7eb94c8fa233: Pull complete
dbd96ac32dbe: Pull complete
778599102d38: Pull complete
8786d2c46035: Pull complete
c3d66bc1fe5d: Pull complete
09bc74e0f4cc: Pull complete
37eaecfa428c: Pull complete
00381ab4380d: Pull complete
9ef8c5c767b5: Pull complete
e3d8190aea64: Pull complete
24f12626dcfb: Pull complete
1304208495f6: Pull complete
a196618e031a: Pull complete
699db20f1266: Pull complete
771d1b87e75a: Pull complete
13204b7f5a63: Pull complete
a02cc6a1bbc4: Pull complete

Digest: sha256:ed9791d01192ec32f238d51ee637658e3dda75d62e859e49018e82b9d198d93a
Status: Downloaded newer image for slaclcls/autosfx:latest
Analyzing slaclcls/autosfx:latest
Docker Version: 19.03.8
GraphDriver: overlay2
Environment Variables
|PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
|DEBIAN_FRONTEND=noninteractive
|LANG=C.UTF-8
|TZ=America/Los_Angeles

Image user
|User is root

Potential secrets:
|Found match etc/ssh/ssh_config Client SSH Config .?ssh_config[\s\S]* 036c6fc38c0c2ff9b0447fc019c9d66d2bbc0ed78fd3ac4d28766ba648659fca/layer.tar
|Found match img/conda.local/miniconda3/pkgs/ncurses-6.2-he6710b0_1/share/terminfo/p/p12 Potential cryptographic key bundle .p12$ 38b12fe28201aa8b254e19eb9ed06d31673f90d010e83758b8b4d1dc3d56632d/layer.tar
|Found match img/conda.local/miniconda3/share/terminfo/p/p12 Potential cryptographic key bundle .p12$ 38b12fe28201aa8b254e19eb9ed06d31673f90d010e83758b8b4d1dc3d56632d/layer.tar
|Found match img/phenix-1.18.2-3874/conda_base/lib/python2.7/site-packages/tornado/test/test.key openssl .key, apple .keychain, etc. \.key$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/conda_base/lib/python2.7/site-packages/wx-3.0-gtk2/wx/tools/Editra/tests/syntax/microsoft_sql.sql Database file \.sql$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/conda_base/lib/python2.7/site-packages/wx-3.0-gtk2/wx/tools/Editra/tests/syntax/sql.sql Database file \.sql$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/conda_base/share/terminfo/p/p12 Potential cryptographic key bundle .p12$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/conditions/condition_variable/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/conditions/condition_variable_any/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/futures/future/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/futures/promise/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/futures/shared_future/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/lock_guard/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/nested_strict_lock/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/shared_lock/cons/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/shared_lock_guard/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/strict_lock/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/unique_lock/cons/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/upgrade_lock/cons/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/null_mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/recursive_mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/recursive_timed_mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/shared_mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/sync/mutual_exclusion/timed_mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/boost/libs/thread/test/threads/thread/constr/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/cctbx_project/xfel/ui/db/schema.sql Database file \.sql$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/cctbx_project/xfel/xpp/experiment_schema.sql Database file \.sql$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/001_lipitor_atorvastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/001_lipitor_atorvastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/002_advair_fluticasone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/002_advair_fluticasone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/002_seretide_salmeterol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/002_seretide_salmeterol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/003_plavix_clopidogrel_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/003_plavix_clopidogrel_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/004_nexium_esomeprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/004_nexium_esomeprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/005_norvasc_amlodipine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/005_norvasc_amlodipine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/006_remicasde_infliximab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/007_enbrel_etanercept_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/008_zyprexa_olanzapine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/008_zyprexa_olanzapine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/009_diovan_valsartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/009_diovan_valsartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/010_risperdal_risperidone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/010_risperdal_risperidone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/011_aranesp_darbepoetin-alfa_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/012_rituxan_rituximab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/013_effexor_venlafaxine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/013_effexor_venlafaxine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/014_protonix_pantoprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/014_protonix_pantoprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/015_singulair_montelukast_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/015_singulair_montelukast_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/016_seroquel_quetiapine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/016_seroquel_quetiapine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/017_prevacid_lansoprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/017_prevacid_lansoprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/018_procrit_erythropoietin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/019_cozaar_losartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/019_cozaar_losartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/020_fosamax_alendronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/020_fosamax_alendronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/021_herceptin_trastuzumab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/022_lovenox_enoxaparin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/022_lovenox_enoxaparin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/023_avandia_rosiglitazone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/023_avandia_rosiglitazone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/024_actos_pioglitazone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/024_actos_pioglitazone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/025_zocor_simvastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/025_zocor_simvastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/026_copaxone_glatiramer_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/026_copaxone_glatiramer_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/027_aciphex_rabeprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/027_aciphex_rabeprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/028_neulasta_filgrastim_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/029_lexapro_escitalopram_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/029_lexapro_escitalopram_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/030_gleevec_imatinib_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/030_gleevec_imatinib_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/031_ambien_zolpidem_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/031_ambien_zolpidem_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/032_aricept_donepezil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/032_aricept_donepezil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/033_epogen_erythropoietin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/034_zyrtec_cetirizine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/034_zyrtec_cetirizine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/035_avapro_irbesartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/035_avapro_irbesartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/036_avastin_bevacizumab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/037_taxotere_docetaxel_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/037_taxotere_docetaxel_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/038_eloxatin_oxaliplatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/038_eloxatin_oxaliplatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/039_zoloft_sertraline_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/039_zoloft_sertraline_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/040_tamiflu_oseltamivir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/040_tamiflu_oseltamivir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/041_lantus_insulin-analog_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/042_crestor_rosuvastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/042_crestor_rosuvastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/043_humira_adalimumab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/044_celebrex_celecoxib_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/044_celebrex_celecoxib_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/045_topomax_topiramate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/045_topomax_topiramate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/046_prevnar_vaccine_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/047_vytorin_ezetimibe_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/047_vytorin_ezetimibe_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/047_vytorin_simvastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/047_vytorin_simvastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/048_zetia_ezetimibe_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/048_zetia_ezetimibe_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/049_wellbutrin_bupropion_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/049_wellbutrin_bupropion_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/050_abilify_aripiprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/050_abilify_aripiprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/051_lamictal_lamotrigine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/051_lamictal_lamotrigine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/052_toprol_metoprolol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/052_toprol_metoprolol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/053_neorecormon_erythropoietin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/054_atacand_candesartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/054_atacand_candesartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/055_spiriva_tiotropium_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/055_spiriva_tiotropium_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/056_avonex_interferon-beta1a_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/057_viagra_sildenafil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/057_viagra_sildenafil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/058_micardis_telmisartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/058_micardis_telmisartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/059_actonel_risedronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/059_actonel_risedronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/060_lupron_leuprolide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/060_lupron_leuprolide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/061_tricor_lipanthyl_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/061_tricor_lipanthyl_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/062_zofran_ondansetron_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/062_zofran_ondansetron_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/063_valtrex_valaciclovir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/063_valtrex_valaciclovir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/064_levaquin_levofloxacin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/064_levaquin_levofloxacin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/065_arimidex_anastrozole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/065_arimidex_anastrozole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/066_prograf_tacrolimus_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/066_prograf_tacrolimus_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/067_cellcept_mycophenolate-mofetil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/067_cellcept_mycophenolate-mofetil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/068_xalatan_latanoprost_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/068_xalatan_latanoprost_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/069_rebif_interferon-beta1a_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/070_coreg_carvedilol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/070_coreg_carvedilol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/071_gemzar_gemcitabine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/071_gemzar_gemcitabine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/072_prilosec_omeprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/072_prilosec_omeprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/073_benicar_olmesartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/073_benicar_olmesartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/074_lotrel_amlodipine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/074_lotrel_amlodipine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/074_lotrel_benazepril_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/074_lotrel_benazepril_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/075_cymbalta_duloxetine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/075_cymbalta_duloxetine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/076_imitrex_sumatriptan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/076_imitrex_sumatriptan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/077_depakote_sodium-valpronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/077_depakote_sodium-valpronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/077_depakote_valproate-semisodium_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/077_depakote_valproate-semisodium_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/077_depakote_valproic-acid_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/077_depakote_valproic-acid_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/078_humalog_lispro-insulin-analog_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/078_humalog_lispro-insulin-analog_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/079_duragesic_fentanyl_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/079_duragesic_fentanyl_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/080_pulmicort_budesonide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/080_pulmicort_budesonide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/081_zometa_zoledronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/081_zometa_zoledronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/082_betaseron_interferon-beta1b_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/083_delix_ramipril_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/083_delix_ramipril_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/084_flovent_fluticasone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/084_flovent_fluticasone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/085_neupogen_filgrastim_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/086_casodex_bicalutamide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/086_casodex_bicalutamide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/087_pravachol_pravastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/087_pravachol_pravastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/088_truvada_emtricitabine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/088_truvada_emtricitabine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/088_truvada_tenofovir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/088_truvada_tenofovir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/089_symbicort_budesonide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/089_symbicort_budesonide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/089_symbicort_formoterol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/089_symbicort_formoterol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/090_pegasys_pegylated-interferon-alfa2a_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/091_evista_raloxifene_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/091_evista_raloxifene_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/092_flomax_tamsulosin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/092_flomax_tamsulosin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/093_lyrica_pregabalin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/093_lyrica_pregabalin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/094_paxil_paroxetine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/094_paxil_paroxetine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/095_kaletra_lopinavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/095_kaletra_lopinavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/095_kaletra_ritonavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/095_kaletra_ritonavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/096_detrol_tolterodine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/096_detrol_tolterodine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/097_harnal_tamsulosin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/097_harnal_tamsulosin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/098_erbitux_cetuximab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/099_synagis_palivizumab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/100_augmentin_amoxicillin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/100_augmentin_amoxicillin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/100_augmentin_clavulanic-acid_CID42617_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/100_augmentin_clavulanic-acid_CID42617_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/100_augmentin_clavulanic-acid_CID52809800_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/100_augmentin_clavulanic-acid_CID52809800_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/100_augmentin_coamoxiclav_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/101_premarin_estrogen-estradiol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/101_premarin_estrogen-estradiol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/101_premarin_estrogen-estriol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/101_premarin_estrogen-estriol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/101_premarin_estrogen-estrone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/101_premarin_estrogen-estrone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/102_ortho-contraceptive_progesterone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/102_ortho-contraceptive_progesterone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/103_zoladex_goserelin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/103_zoladex_goserelin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/104_cerezyme_imiglucerase_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/105_cravit_levofloxacin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/105_cravit_levofloxacin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/106_yasmin_drospirenone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/106_yasmin_drospirenone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/107_kogenate_recombinant-factor-viii_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/108_botox_botulin-toxin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/109_lamisil_terbinafine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/109_lamisil_terbinafine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/110_combivir_lamivudine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/110_combivir_lamivudine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/110_combivir_zidovudine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/110_combivir_zidovudine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/111_zosyn_piperacillin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/111_zosyn_piperacillin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/112_cialis_tadalafil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/112_cialis_tadalafil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/113_keppra_levetiracetam_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/113_keppra_levetiracetam_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/114_novoseven_factor-vii_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/115_infanrix_vaccine_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/116_nasonex_mometasone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/116_nasonex_mometasone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/117_reyataz_atazanavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/117_reyataz_atazanavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/118_concerta_methylphenidate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/118_concerta_methylphenidate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/119_humulin_recombinant-human-insulin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/120_neoral_ciclosporin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/120_neoral_ciclosporin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/121_longastatin_octreotide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/121_longastatin_octreotide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/121_sandostatin_somatostatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/122_camptosar_irinotecan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/122_camptosar_irinotecan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/123_egenerix-b_vaccine_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/124_allegra_fexofenadine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/124_allegra_fexofenadine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/125_adderall_amphetamine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/125_adderall_amphetamine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/126_combivent_ipratropium_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/126_combivent_ipratropium_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/126_combivent_salbutamol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/126_combivent_salbutamol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/127_peg-intron_pegylated-interferon-alfa2b_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/128_adalat_nifedipine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/128_adalat_nifedipine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/129_avelox_moxifloxacin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/129_avelox_moxifloxacin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/130_mobic_meloxicam_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/130_mobic_meloxicam_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/131_biaxin_clarithromycin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/131_biaxin_clarithromycin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/132_mevalotin_pravastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/132_mevalotin_pravastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/133_ultane_sevoflurane_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/133_ultane_sevoflurane_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/134_genotropin_somatropin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/135_sustiva_efavirenz_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/135_sustiva_efavirenz_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/136_zyvox_linezolid_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/136_zyvox_linezolid_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/137_xeloda_capecitabine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/137_xeloda_capecitabine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/138_geodon_ziprasidone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/138_geodon_ziprasidone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/139_cipro_ciprofloxacin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/139_cipro_ciprofloxacin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/140_provigil_modafinil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/140_provigil_modafinil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/141_lescol_fluvastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/141_lescol_fluvastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/142_clarinex_desloratadine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/142_clarinex_desloratadine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/143_femara_letrozole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/143_femara_letrozole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/144_trileptal_oxcarbazepine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/144_trileptal_oxcarbazepine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/145_tracleer.bosentan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/145_tracleer.bosentan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/146_primaxin_cilastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/146_primaxin_cilastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/146_primaxin_imipenem_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/146_primaxin_imipenem_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/147_temadar_temozolomide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/147_temadar_temozolomide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/148_trusopt_dorzolamide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/148_trusopt_dorzolamide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/149_voltaren_diclofenac_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/149_voltaren_diclofenac_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/150_viread_tenofovir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/150_viread_tenofovir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/151_sifrol_pramipexole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/151_sifrol_pramipexole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/152_nameda_memantine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/152_nameda_memantine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/153_altace_ramipril_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/153_altace_ramipril_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/154_byetta_exenatide_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/155_tarceva_erlotinib_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/155_tarceva_erlotinib_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/156_llosone_erythromycin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/156_llosone_erythromycin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/156_zithromax_azithromycin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/156_zithromax_azithromycin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/157_omnicef_cefdinir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/157_omnicef_cefdinir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/158_proscar_finasteride_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/158_proscar_finasteride_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/159_alimta_pemetrexed_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/159_alimta_pemetrexed_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/160_merrem_meropenem_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/160_merrem_meropenem_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/161_forteo_teriparatide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/161_forteo_teriparatide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/162_strattera_atomoxetine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/162_strattera_atomoxetine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/163_actiq_fentanyl_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/163_actiq_fentanyl_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/164_flonase_fluticasone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/164_flonase_fluticasone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/165_amaryl_glimepiride_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/165_amaryl_glimepiride_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/166_lidoderm_lidocaine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/166_lidoderm_lidocaine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/167_lunesta_eszopiclone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/167_lunesta_eszopiclone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/168_boniva_ibandronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/168_boniva_ibandronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/169_taxol_paclitaxel_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/169_taxol_paclitaxel_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/170_zelnorm_tegaserod-maleate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/170_zelnorm_tegaserod_CID5362436_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/170_zelnorm_tegaserod_CID5362436_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/170_zelnorm_tegaserod_CID5487301_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/170_zelnorm_tegaserod_CID5487301_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/171_renagel_sevelamer_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/171_renagel_sevelamer_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/172_norditropin_human-growth-hormone_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/173_xopenex_levalbuterol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/173_xopenex_levalbuterol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/174_xenical_orlistat_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/174_xenical_orlistat_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/175_vasotec_enalapril_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/175_vasotec_enalapril_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/176_serevent_salmeterol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/176_serevent_salmeterol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/177_cardura_doxazosin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/177_cardura_doxazosin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/178_synthroid_levothyroxine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/178_synthroid_levothyroxine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/179_gonal-f_follitropin-alpha_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/180_gaster_famotidine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/180_gaster_famotidine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/181_cancidas_caspofungin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/181_cancidas_caspofungin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/182_exelon_rivastigmine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/182_exelon_rivastigmine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/183_vfend_voriconazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/183_vfend_voriconazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/184_amlodin_amlodipine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/184_amlodin_amlodipine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/185_niaspan_niacin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/185_niaspan_niacin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/186_neurontin_gabapentin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/186_neurontin_gabapentin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/187_trizivir_abacavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/187_trizivir_abacavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/187_trizivir_lamivudine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/187_trizivir_lamivudine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/187_trizivir_zidovudine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/187_trizivir_zidovudine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/188_requip_ropinirole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/188_requip_ropinirole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/189_follistim_follitropin-beta_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/190_basen_voglibose_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/190_basen_voglibose_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/191_levitra_vardenafil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/191_levitra_vardenafil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/192_glucophage_metformin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/192_glucophage_metformin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/193_concor_bisoprolol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/193_concor_bisoprolol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/194_epzicom_abacavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/194_epzicom_abacavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/194_epzicom_lamivudine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/194_epzicom_lamivudine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/195_xatral_alfuzosin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/195_xatral_alfuzosin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/196_diflucan_fluconazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/196_diflucan_fluconazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/197_thalomid_thalidomide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/197_thalomid_thalidomide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/198_zantac_ranitidine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/198_zantac_ranitidine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/199_xolair_omalizumab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/200_claritin_loratadine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/200_claritin_loratadine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/401_reveyes_dapiprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/401_reveyes_dapiprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/402_epilim_sodium-valpronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/402_epilim_sodium-valpronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/403_prezista_darunavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/403_prezista_darunavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/404_aptivus_tipranavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/404_aptivus_tipranavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/405_lexiva_fosamprenavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/405_lexiva_fosamprenavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/406_agenerase_amprenavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/406_agenerase_amprenavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/407_viracept_nelfinavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/407_viracept_nelfinavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/408_crixivan_indinavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/408_crixivan_indinavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/408_fortovase_saquinavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/chem_data/top_drugs/408_fortovase_saquinavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_1044_purine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_1044_purine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_11378474_isobenzofuran_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_11378474_isobenzofuran_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_136081_isobenzothiophene_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_136081_isobenzothiophene_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_23646543_pyrrolotriazine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_23646543_pyrrolotriazine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_3013853_isoindole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_3013853_isoindole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_455565_imidazopyridazine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_455565_imidazopyridazine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_5004_quinalizarin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_5004_quinalizarin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_5798_benzimidazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_5798_benzimidazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_71073_benzisoxazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_71073_benzisoxazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_7221_benzothiophene_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_7221_benzothiophene_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_7222_benzothiazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_7222_benzothiazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_798_indole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_798_indole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_9221_indazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_9221_indazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_9223_benzofuran_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_9223_benzofuran_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_9228_benzoxazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/CID_9228_benzoxazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/elbow/resources/fused_rings/cyclohexane.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/phenix_regression/wizards/command_line_ligands_tests/test_ligand_list/a1000.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-1.18.2-3874/modules/phenix_regression/wizards/command_line_ligands_tests/test_ligand_list/a1001.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/conditions/condition_variable/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/conditions/condition_variable_any/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/futures/future/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/futures/promise/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/futures/shared_future/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/lock_guard/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/nested_strict_lock/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/shared_lock/cons/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/shared_lock_guard/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/strict_lock/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/unique_lock/cons/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/locks/upgrade_lock/cons/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/null_mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/recursive_mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/recursive_timed_mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/shared_mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/sync/mutual_exclusion/timed_mutex/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/boost/libs/thread/test/threads/thread/constr/default_pass.cpp dbman default.pass 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/cctbx_project/xfel/ui/db/schema.sql Database file \.sql$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/cctbx_project/xfel/xpp/experiment_schema.sql Database file \.sql$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/001_lipitor_atorvastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/001_lipitor_atorvastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/002_advair_fluticasone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/002_advair_fluticasone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/002_seretide_salmeterol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/002_seretide_salmeterol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/003_plavix_clopidogrel_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/003_plavix_clopidogrel_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/004_nexium_esomeprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/004_nexium_esomeprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/005_norvasc_amlodipine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/005_norvasc_amlodipine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/006_remicasde_infliximab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/007_enbrel_etanercept_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/008_zyprexa_olanzapine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/008_zyprexa_olanzapine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/009_diovan_valsartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/009_diovan_valsartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/010_risperdal_risperidone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/010_risperdal_risperidone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/011_aranesp_darbepoetin-alfa_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/012_rituxan_rituximab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/013_effexor_venlafaxine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/013_effexor_venlafaxine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/014_protonix_pantoprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/014_protonix_pantoprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/015_singulair_montelukast_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/015_singulair_montelukast_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/016_seroquel_quetiapine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/016_seroquel_quetiapine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/017_prevacid_lansoprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/017_prevacid_lansoprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/018_procrit_erythropoietin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/019_cozaar_losartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/019_cozaar_losartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/020_fosamax_alendronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/020_fosamax_alendronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/021_herceptin_trastuzumab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/022_lovenox_enoxaparin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/022_lovenox_enoxaparin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/023_avandia_rosiglitazone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/023_avandia_rosiglitazone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/024_actos_pioglitazone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/024_actos_pioglitazone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/025_zocor_simvastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/025_zocor_simvastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/026_copaxone_glatiramer_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/026_copaxone_glatiramer_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/027_aciphex_rabeprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/027_aciphex_rabeprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/028_neulasta_filgrastim_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/029_lexapro_escitalopram_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/029_lexapro_escitalopram_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/030_gleevec_imatinib_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/030_gleevec_imatinib_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/031_ambien_zolpidem_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/031_ambien_zolpidem_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/032_aricept_donepezil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/032_aricept_donepezil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/033_epogen_erythropoietin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/034_zyrtec_cetirizine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/034_zyrtec_cetirizine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/035_avapro_irbesartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/035_avapro_irbesartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/036_avastin_bevacizumab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/037_taxotere_docetaxel_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/037_taxotere_docetaxel_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/038_eloxatin_oxaliplatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/038_eloxatin_oxaliplatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/039_zoloft_sertraline_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/039_zoloft_sertraline_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/040_tamiflu_oseltamivir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/040_tamiflu_oseltamivir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/041_lantus_insulin-analog_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/042_crestor_rosuvastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/042_crestor_rosuvastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/043_humira_adalimumab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/044_celebrex_celecoxib_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/044_celebrex_celecoxib_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/045_topomax_topiramate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/045_topomax_topiramate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/046_prevnar_vaccine_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/047_vytorin_ezetimibe_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/047_vytorin_ezetimibe_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/047_vytorin_simvastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/047_vytorin_simvastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/048_zetia_ezetimibe_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/048_zetia_ezetimibe_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/049_wellbutrin_bupropion_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/049_wellbutrin_bupropion_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/050_abilify_aripiprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/050_abilify_aripiprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/051_lamictal_lamotrigine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/051_lamictal_lamotrigine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/052_toprol_metoprolol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/052_toprol_metoprolol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/053_neorecormon_erythropoietin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/054_atacand_candesartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/054_atacand_candesartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/055_spiriva_tiotropium_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/055_spiriva_tiotropium_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/056_avonex_interferon-beta1a_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/057_viagra_sildenafil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/057_viagra_sildenafil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/058_micardis_telmisartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/058_micardis_telmisartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/059_actonel_risedronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/059_actonel_risedronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/060_lupron_leuprolide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/060_lupron_leuprolide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/061_tricor_lipanthyl_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/061_tricor_lipanthyl_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/062_zofran_ondansetron_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/062_zofran_ondansetron_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/063_valtrex_valaciclovir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/063_valtrex_valaciclovir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/064_levaquin_levofloxacin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/064_levaquin_levofloxacin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/065_arimidex_anastrozole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/065_arimidex_anastrozole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/066_prograf_tacrolimus_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/066_prograf_tacrolimus_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/067_cellcept_mycophenolate-mofetil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/067_cellcept_mycophenolate-mofetil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/068_xalatan_latanoprost_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/068_xalatan_latanoprost_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/069_rebif_interferon-beta1a_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/070_coreg_carvedilol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/070_coreg_carvedilol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/071_gemzar_gemcitabine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/071_gemzar_gemcitabine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/072_prilosec_omeprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/072_prilosec_omeprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/073_benicar_olmesartan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/073_benicar_olmesartan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/074_lotrel_amlodipine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/074_lotrel_amlodipine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/074_lotrel_benazepril_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/074_lotrel_benazepril_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/075_cymbalta_duloxetine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/075_cymbalta_duloxetine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/076_imitrex_sumatriptan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/076_imitrex_sumatriptan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/077_depakote_sodium-valpronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/077_depakote_sodium-valpronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/077_depakote_valproate-semisodium_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/077_depakote_valproate-semisodium_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/077_depakote_valproic-acid_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/077_depakote_valproic-acid_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/078_humalog_lispro-insulin-analog_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/078_humalog_lispro-insulin-analog_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/079_duragesic_fentanyl_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/079_duragesic_fentanyl_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/080_pulmicort_budesonide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/080_pulmicort_budesonide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/081_zometa_zoledronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/081_zometa_zoledronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/082_betaseron_interferon-beta1b_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/083_delix_ramipril_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/083_delix_ramipril_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/084_flovent_fluticasone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/084_flovent_fluticasone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/085_neupogen_filgrastim_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/086_casodex_bicalutamide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/086_casodex_bicalutamide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/087_pravachol_pravastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/087_pravachol_pravastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/088_truvada_emtricitabine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/088_truvada_emtricitabine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/088_truvada_tenofovir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/088_truvada_tenofovir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/089_symbicort_budesonide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/089_symbicort_budesonide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/089_symbicort_formoterol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/089_symbicort_formoterol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/090_pegasys_pegylated-interferon-alfa2a_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/091_evista_raloxifene_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/091_evista_raloxifene_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/092_flomax_tamsulosin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/092_flomax_tamsulosin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/093_lyrica_pregabalin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/093_lyrica_pregabalin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/094_paxil_paroxetine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/094_paxil_paroxetine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/095_kaletra_lopinavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/095_kaletra_lopinavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/095_kaletra_ritonavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/095_kaletra_ritonavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/096_detrol_tolterodine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/096_detrol_tolterodine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/097_harnal_tamsulosin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/097_harnal_tamsulosin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/098_erbitux_cetuximab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/099_synagis_palivizumab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/100_augmentin_amoxicillin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/100_augmentin_amoxicillin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/100_augmentin_clavulanic-acid_CID42617_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/100_augmentin_clavulanic-acid_CID42617_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/100_augmentin_clavulanic-acid_CID52809800_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/100_augmentin_clavulanic-acid_CID52809800_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/100_augmentin_coamoxiclav_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/101_premarin_estrogen-estradiol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/101_premarin_estrogen-estradiol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/101_premarin_estrogen-estriol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/101_premarin_estrogen-estriol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/101_premarin_estrogen-estrone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/101_premarin_estrogen-estrone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/102_ortho-contraceptive_progesterone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/102_ortho-contraceptive_progesterone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/103_zoladex_goserelin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/103_zoladex_goserelin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/104_cerezyme_imiglucerase_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/105_cravit_levofloxacin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/105_cravit_levofloxacin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/106_yasmin_drospirenone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/106_yasmin_drospirenone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/107_kogenate_recombinant-factor-viii_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/108_botox_botulin-toxin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/109_lamisil_terbinafine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/109_lamisil_terbinafine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/110_combivir_lamivudine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/110_combivir_lamivudine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/110_combivir_zidovudine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/110_combivir_zidovudine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/111_zosyn_piperacillin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/111_zosyn_piperacillin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/112_cialis_tadalafil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/112_cialis_tadalafil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/113_keppra_levetiracetam_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/113_keppra_levetiracetam_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/114_novoseven_factor-vii_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/115_infanrix_vaccine_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/116_nasonex_mometasone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/116_nasonex_mometasone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/117_reyataz_atazanavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/117_reyataz_atazanavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/118_concerta_methylphenidate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/118_concerta_methylphenidate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/119_humulin_recombinant-human-insulin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/120_neoral_ciclosporin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/120_neoral_ciclosporin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/121_longastatin_octreotide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/121_longastatin_octreotide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/121_sandostatin_somatostatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/122_camptosar_irinotecan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/122_camptosar_irinotecan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/123_egenerix-b_vaccine_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/124_allegra_fexofenadine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/124_allegra_fexofenadine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/125_adderall_amphetamine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/125_adderall_amphetamine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/126_combivent_ipratropium_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/126_combivent_ipratropium_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/126_combivent_salbutamol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/126_combivent_salbutamol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/127_peg-intron_pegylated-interferon-alfa2b_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/128_adalat_nifedipine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/128_adalat_nifedipine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/129_avelox_moxifloxacin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/129_avelox_moxifloxacin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/130_mobic_meloxicam_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/130_mobic_meloxicam_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/131_biaxin_clarithromycin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/131_biaxin_clarithromycin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/132_mevalotin_pravastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/132_mevalotin_pravastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/133_ultane_sevoflurane_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/133_ultane_sevoflurane_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/134_genotropin_somatropin_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/135_sustiva_efavirenz_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/135_sustiva_efavirenz_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/136_zyvox_linezolid_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/136_zyvox_linezolid_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/137_xeloda_capecitabine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/137_xeloda_capecitabine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/138_geodon_ziprasidone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/138_geodon_ziprasidone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/139_cipro_ciprofloxacin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/139_cipro_ciprofloxacin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/140_provigil_modafinil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/140_provigil_modafinil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/141_lescol_fluvastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/141_lescol_fluvastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/142_clarinex_desloratadine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/142_clarinex_desloratadine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/143_femara_letrozole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/143_femara_letrozole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/144_trileptal_oxcarbazepine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/144_trileptal_oxcarbazepine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/145_tracleer.bosentan_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/145_tracleer.bosentan_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/146_primaxin_cilastatin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/146_primaxin_cilastatin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/146_primaxin_imipenem_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/146_primaxin_imipenem_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/147_temadar_temozolomide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/147_temadar_temozolomide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/148_trusopt_dorzolamide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/148_trusopt_dorzolamide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/149_voltaren_diclofenac_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/149_voltaren_diclofenac_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/150_viread_tenofovir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/150_viread_tenofovir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/151_sifrol_pramipexole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/151_sifrol_pramipexole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/152_nameda_memantine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/152_nameda_memantine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/153_altace_ramipril_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/153_altace_ramipril_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/154_byetta_exenatide_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/155_tarceva_erlotinib_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/155_tarceva_erlotinib_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/156_llosone_erythromycin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/156_llosone_erythromycin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/156_zithromax_azithromycin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/156_zithromax_azithromycin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/157_omnicef_cefdinir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/157_omnicef_cefdinir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/158_proscar_finasteride_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/158_proscar_finasteride_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/159_alimta_pemetrexed_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/159_alimta_pemetrexed_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/160_merrem_meropenem_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/160_merrem_meropenem_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/161_forteo_teriparatide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/161_forteo_teriparatide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/162_strattera_atomoxetine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/162_strattera_atomoxetine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/163_actiq_fentanyl_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/163_actiq_fentanyl_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/164_flonase_fluticasone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/164_flonase_fluticasone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/165_amaryl_glimepiride_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/165_amaryl_glimepiride_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/166_lidoderm_lidocaine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/166_lidoderm_lidocaine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/167_lunesta_eszopiclone_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/167_lunesta_eszopiclone_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/168_boniva_ibandronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/168_boniva_ibandronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/169_taxol_paclitaxel_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/169_taxol_paclitaxel_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/170_zelnorm_tegaserod-maleate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/170_zelnorm_tegaserod_CID5362436_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/170_zelnorm_tegaserod_CID5362436_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/170_zelnorm_tegaserod_CID5487301_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/170_zelnorm_tegaserod_CID5487301_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/171_renagel_sevelamer_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/171_renagel_sevelamer_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/172_norditropin_human-growth-hormone_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/173_xopenex_levalbuterol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/173_xopenex_levalbuterol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/174_xenical_orlistat_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/174_xenical_orlistat_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/175_vasotec_enalapril_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/175_vasotec_enalapril_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/176_serevent_salmeterol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/176_serevent_salmeterol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/177_cardura_doxazosin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/177_cardura_doxazosin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/178_synthroid_levothyroxine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/178_synthroid_levothyroxine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/179_gonal-f_follitropin-alpha_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/180_gaster_famotidine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/180_gaster_famotidine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/181_cancidas_caspofungin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/181_cancidas_caspofungin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/182_exelon_rivastigmine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/182_exelon_rivastigmine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/183_vfend_voriconazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/183_vfend_voriconazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/184_amlodin_amlodipine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/184_amlodin_amlodipine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/185_niaspan_niacin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/185_niaspan_niacin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/186_neurontin_gabapentin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/186_neurontin_gabapentin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/187_trizivir_abacavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/187_trizivir_abacavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/187_trizivir_lamivudine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/187_trizivir_lamivudine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/187_trizivir_zidovudine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/187_trizivir_zidovudine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/188_requip_ropinirole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/188_requip_ropinirole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/189_follistim_follitropin-beta_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/190_basen_voglibose_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/190_basen_voglibose_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/191_levitra_vardenafil_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/191_levitra_vardenafil_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/192_glucophage_metformin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/192_glucophage_metformin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/193_concor_bisoprolol_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/193_concor_bisoprolol_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/194_epzicom_abacavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/194_epzicom_abacavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/194_epzicom_lamivudine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/194_epzicom_lamivudine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/195_xatral_alfuzosin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/195_xatral_alfuzosin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/196_diflucan_fluconazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/196_diflucan_fluconazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/197_thalomid_thalidomide_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/197_thalomid_thalidomide_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/198_zantac_ranitidine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/198_zantac_ranitidine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/199_xolair_omalizumab_bad.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/200_claritin_loratadine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/200_claritin_loratadine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/401_reveyes_dapiprazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/401_reveyes_dapiprazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/402_epilim_sodium-valpronate_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/402_epilim_sodium-valpronate_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/403_prezista_darunavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/403_prezista_darunavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/404_aptivus_tipranavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/404_aptivus_tipranavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/405_lexiva_fosamprenavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/405_lexiva_fosamprenavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/406_agenerase_amprenavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/406_agenerase_amprenavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/407_viracept_nelfinavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/407_viracept_nelfinavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/408_crixivan_indinavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/408_crixivan_indinavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/408_fortovase_saquinavir_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/chem_data/top_drugs/408_fortovase_saquinavir_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_1044_purine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_1044_purine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_11378474_isobenzofuran_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_11378474_isobenzofuran_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_136081_isobenzothiophene_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_136081_isobenzothiophene_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_23646543_pyrrolotriazine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_23646543_pyrrolotriazine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_3013853_isoindole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_3013853_isoindole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_455565_imidazopyridazine_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_455565_imidazopyridazine_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_5004_quinalizarin_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_5004_quinalizarin_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_5798_benzimidazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_5798_benzimidazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_71073_benzisoxazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_71073_benzisoxazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_7221_benzothiophene_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_7221_benzothiophene_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_7222_benzothiazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_7222_benzothiazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_798_indole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_798_indole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_9221_indazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_9221_indazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_9223_benzofuran_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_9223_benzofuran_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_9228_benzoxazole_2D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/CID_9228_benzoxazole_3D.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/elbow/resources/fused_rings/cyclohexane.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/phenix_regression/wizards/command_line_ligands_tests/test_ligand_list/a1000.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6/modules/phenix_regression/wizards/command_line_ligands_tests/test_ligand_list/a1001.sdf Database file \.sdf$ 5c1b8413c8199a270ac279ef10bc253993910ca9e69efa603ee423814283bfe6/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/etc/jupyter/nbconfig/notebook.d/plotlywidget.json Jupyter Configuration file jupyter[^ ]*config[^ ]*.json 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/etc/jupyter/nbconfig/notebook.d/widgetsnbextension.json Jupyter Configuration file jupyter[^ ]*config[^ ]*.json 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/etc/jupyter/nbconfig/notebook.json Jupyter Configuration file jupyter[^ ]*config[^ ]*.json 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/lib/python2.7/site-packages/gevent/tests/server.key openssl .key, apple .keychain, etc. \.key$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/lib/python2.7/site-packages/gevent/tests/test_server.key openssl .key, apple .keychain, etc. \.key$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/lib/python2.7/site-packages/tornado/test/test.key openssl .key, apple .keychain, etc. \.key$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/share/cmake-3.17/Templates/Windows/Windows_TemporaryKey.pfx Private client certificate \.pfx$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/share/mysql/innodb_memcached_config.sql Database file \.sql$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/share/mysql/install_rewriter.sql Database file \.sql$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/share/mysql/uninstall_rewriter.sql Database file \.sql$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/share/terminfo/p/p12 Potential cryptographic key bundle .p12$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/pkgs/cmake-3.17.0-h28c56e5_0/share/cmake-3.17/Templates/Windows/Windows_TemporaryKey.pfx Private client certificate \.pfx$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/pkgs/gevent-1.4.0-py27h516909a_0/lib/python2.7/site-packages/gevent/tests/server.key openssl .key, apple .keychain, etc. \.key$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/pkgs/gevent-1.4.0-py27h516909a_0/lib/python2.7/site-packages/gevent/tests/test_server.key openssl .key, apple .keychain, etc. \.key$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/pkgs/mysql-8.0.20-0/share/mysql/install_rewriter.sql Database file \.sql$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/pkgs/mysql-8.0.20-0/share/mysql/uninstall_rewriter.sql Database file \.sql$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/pkgs/mysql-server-8.0.20-he5fb6c4_0/share/mysql/innodb_memcached_config.sql Database file \.sql$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/pkgs/plotly-4.8.2-pyh9f0ad1d_0/etc/jupyter/nbconfig/notebook.d/plotlywidget.json Jupyter Configuration file jupyter[^ ]*config[^ ]*.json 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/pkgs/tornado-5.1.1-py27h14c3975_1000/lib/python2.7/site-packages/tornado/test/test.key openssl .key, apple .keychain, etc. \.key$ 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/pkgs/widgetsnbextension-3.5.1-py27_0/etc/jupyter/nbconfig/notebook.d/widgetsnbextension.json Jupyter Configuration file jupyter[^ ]*config[^ ]*.json 771493e66bb5af00d69731eebb7d3ae7fc6bb906014a2262b5d4ca5eb8457df2/layer.tar
|Found match img/conda.local/miniconda3/envs/psana_base/etc/jupyter/jupyter_notebook_config.d/jupyterlab.json Jupyter Configuration file jupyter[^ ]*config[^ ]*.json 7c6bf176c4de2bd62e5c5ca588e760abaed6008c77c9ee104dbadd1053298e2a/layer.tar
|Found match img/conda.local/miniconda3/pkgs/ncurses-6.1-hf484d3e_1002/share/terminfo/p/p12 Potential cryptographic key bundle .p12$ 86b5ed683bcdfc12823bfa7cbb5d462b106a938d2a7ce1ca108b9aec5f964dd1/layer.tar
|Found match img/conda.local/miniconda3/share/terminfo/p/p12 Potential cryptographic key bundle .p12$ 86b5ed683bcdfc12823bfa7cbb5d462b106a938d2a7ce1ca108b9aec5f964dd1/layer.tar
|Found match img/ccp4-7.1/bin/p842asc Potential cryptographic key bundle .asc$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/conditions/condition_variable/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/conditions/condition_variable_any/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/futures/future/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/futures/promise/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/futures/shared_future/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/locks/lock_guard/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/locks/nested_strict_lock/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/locks/shared_lock/cons/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/locks/shared_lock_guard/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/locks/strict_lock/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/locks/unique_lock/cons/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/locks/upgrade_lock/cons/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/mutex/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/null_mutex/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/recursive_mutex/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/recursive_timed_mutex/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/shared_mutex/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/sync/mutual_exclusion/timed_mutex/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/boost/libs/thread/test/threads/thread/constr/default_pass.cpp dbman default.pass 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/cctbx_project/xfel/ui/db/schema.sql Database file \.sql$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/py2/site-packages/cctbx_project/xfel/xpp/experiment_schema.sql Database file \.sql$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/python2.7/site-packages/wx-3.0-gtk2/wx/tools/Editra/tests/syntax/microsoft_sql.sql Database file \.sql$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/lib/python2.7/site-packages/wx-3.0-gtk2/wx/tools/Editra/tests/syntax/sql.sql Database file \.sql$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/share/RDKit/Contrib/PBF/testData/egfr.sdf Database file \.sdf$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/share/RDKit/Data/NCI/first_200.props.sdf Database file \.sdf$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/share/RDKit/Data/rddata.sql Database file \.sql$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/share/RDKit/Projects/DbCLI/testData/bzr.sdf Database file \.sdf$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/share/RDKit/Projects/DbCLI/testData/pubchem.200.sdf Database file \.sdf$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/share/ccp4i2/dbapi/database_schema.sql Database file \.sql$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/share/ccp4i2/dbapi/temp_database_schema.sql Database file \.sql$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
|Found match img/ccp4-7.1/share/dbccp4i/dbccp4i/schema.sql Database file \.sql$ 941df99eb22af788e21f46a00ac62ba115522f4b0077a64e8d0660bedd9e2dec/layer.tar
Dockerfile:
RUN [ -z "$(apt-get indextargets)" ]
RUN set -xe  \
	&& echo '#!/bin/sh' > /usr/sbin/policy-rc.d  \
	&& echo 'exit 101' >> /usr/sbin/policy-rc.d  \
	&& chmod +x /usr/sbin/policy-rc.d  \
	&& dpkg-divert --local --rename --add /sbin/initctl  \
	&& cp -a /usr/sbin/policy-rc.d /sbin/initctl  \
	&& sed -i 's/^exit.*/exit 0/' /sbin/initctl  \
	&& echo 'force-unsafe-io' > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup  \
	&& echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' > /etc/apt/apt.conf.d/docker-clean  \
	&& echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >> /etc/apt/apt.conf.d/docker-clean  \
	&& echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";' >> /etc/apt/apt.conf.d/docker-clean  \
	&& echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages  \
	&& echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' > /etc/apt/apt.conf.d/docker-gzip-indexes  \
	&& echo 'Apt::AutoRemove::SuggestsImportant "false";' > /etc/apt/apt.conf.d/docker-autoremove-suggests
RUN mkdir -p /run/systemd  \
	&& echo 'docker' > /run/systemd/container
CMD ["/bin/bash"]
LABEL maintainer=Johannes Blaschke <jpblaschke@lbl.gov>
ARG PYVER=3.7
ARG PSANA_PKG_NAME=
ARG PSANA_VERSION=
ARG EXTRA_YAML=
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 RUN apt-get update  \
	&& apt-get --yes upgrade  \
	&& apt-get --yes install bzip2 curl git libffi-dev lsb-release tzdata vim wget bash autoconf automake gcc g++ make gfortran tar strace
ENV TZ=America/Los_Angeles
|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime  \
	&& echo $TZ > /etc/timezone
/bin/bash -c #(nop) SHELL [/bin/bash -c]
|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c mkdir /img
/bin/bash -c #(nop) COPY dir:09745796546aecce582295a194ff7cd42baeba1482fd68f20ee8c85c10d82bc1 in /img/conda.local
	img/
	img/conda.local/
	img/conda.local/.wh..wh..opq
	img/conda.local/.git
	img/conda.local/README.md
	img/conda.local/env.sh
	img/conda.local/install_conda.sh
	img/conda.local/nuke_all.sh
	img/conda.local/sites/
	img/conda.local/sites/default.sh
	img/conda.local/sites/nersc.sh
	img/conda.local/sites/olcf.sh
	img/conda.local/unenv.sh
	img/conda.local/update_installer.sh

|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  \
	&& mv Miniconda3-latest-Linux-x86_64.sh /img/conda.local/  \
	&& chmod +x /img/conda.local/Miniconda3-latest-Linux-x86_64.sh
|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh  \
	&& mv Miniconda3-latest-Linux-ppc64le.sh /img/conda.local/  \
	&& chmod +x /img/conda.local/Miniconda3-latest-Linux-ppc64le.sh
|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c cd /img/conda.local  \
	&& . sites/default.sh  \
	&& export STATIC_DIR=../../static  \
	&& ./install_conda.sh
|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c mkdir -p /img/opt/env
/bin/bash -c #(nop) COPY dir:2007e44e233a01f8c9cc9850d9eb03df64a05911817c2f465033b96e82918c00 in /img/opt/env
	img/
	img/opt/

|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c cd /img/opt/env  \
	&& ./setup_env.sh
|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c mkdir -p /img/opt
/bin/bash -c #(nop) COPY file:39d52f08cd317564fc36cd56cc48055e48299cdc3a5be6235e10698bc43e1208 in /img/opt/
	img/
	img/opt/
	img/opt/setup_lcls2.sh

|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c cd /img/opt/  \
	&& ./setup_lcls2.sh
/bin/bash -c #(nop) COPY file:77c1231eb703b67bb3854bba5916443ad2ac4b3a7cbdb1a5beef34acc3471b3a in /img/opt/
	img/
	img/opt/
	img/opt/mk_env.sh

|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c cd /img/opt/  \
	&& ./mk_env.sh
|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c mkdir -p /img/opt
/bin/bash -c #(nop) COPY file:16d839f47a5afac39d4760165c9ebf0a76d52f561d352ce12c280b5a29d48eac in /img/opt/
	img/
	img/opt/
	img/opt/setup_extras.sh

|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c mkdir -p /img/opt/pkg_data/
/bin/bash -c #(nop) COPY file:c26f72c16c70b915a2e8a1ccd6c41e27dad399e8d19c5d1abc00d48560b9e567 in /img/opt/pkg_data/
	img/
	img/opt/
	img/opt/pkg_data/
	img/opt/pkg_data/pip.txt

|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c cd /img/opt/  \
	&& ./setup_extras.sh
|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c /sbin/ldconfig
|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c mkdir -p /img
/bin/bash -c #(nop) ADD file:163eb2d54a9b19029279d0490cbb6cdab530e01384edee208d988ac7a3bf0618 in /img
	img/
	img/entrypoint.sh

/bin/bash -c #(nop) COPY file:fdaf4ed2146b618a7561e0db97a6b5a6323f464acaeda2e6ce9ff33107d7deb7 in /img/opt/launch_jupyter.sh
	img/
	img/opt/
	img/opt/launch_jupyter.sh

|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c ln -s /img/opt/launch_jupyter.sh /img/launch_jupyter.sh
/bin/bash -c #(nop) WORKDIR /img
|4 EXTRA_YAML=https://raw.githubusercontent.com/slaclab/anarel-manage/py3/jenkins/ana-env-py2.yaml PSANA_PKG_NAME=psana-conda PSANA_VERSION=2.0.6 PYVER=2.7 /bin/bash -c chmod +x entrypoint.sh
/bin/bash -c #(nop) ENTRYPOINT ["./entrypoint.sh"]
/bin/bash -c #(nop) LABEL maintainer=Frederic Poitevin <frederic.poitevin@stanford.edu>
/bin/bash -c apt-get --yes install build-essential libhdf5-dev libgsl-dev libgtk2.0-dev libcairo2-dev libpango1.0-dev libgdk-pixbuf2.0-dev libfftw3-dev libcbf-dev libncurses5-dev libpng-dev libtiff5-dev cmake
/bin/bash -c #(nop) WORKDIR /img
/bin/bash -c wget https://www.desy.de/~twhite/crystfel/crystfel-0.8.0.tar.gz  \
	&& tar -xzvf crystfel-0.8.0.tar.gz  \
	&& cd crystfel-0.8.0  \
	&& mkdir build  \
	&& cd build  \
	&& cmake ..  \
	&& make install  \
	&& cd /img  \
	&& rm -rf crystfel-0.8.0.tar.gz
/bin/bash -c wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1XvZ1FJFFaunq151e4WrjFkpc-My3m8XQ' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1XvZ1FJFFaunq151e4WrjFkpc-My3m8XQ" -O ccp4-7.1.002-shelx-linux64.tar.gz  \
	&& rm -rf /tmp/cookies.txt  \
	&& tar -xzvf ccp4-7.1.002-shelx-linux64.tar.gz  \
	&& cd ccp4-7.1  \
	&& ./BINARY.setup --run-from-script  \
	&& . bin/ccp4.setup-sh  \
	&& cd /img  \
	&& rm -rf ccp4-7.1.002-shelx-linux64.tar.gz
/bin/bash -c wget ftp://ftp.mpimf-heidelberg.mpg.de/pub/kabsch/XDS-INTEL64_Linux_x86_64.tar.gz  \
	&& tar -xvf XDS-INTEL64_Linux_x86_64.tar.gz  \
	&& export PATH=/img/XDS-INTEL64_Linux_x86_64/:$PATH  \
	&& export KMP_STACKSIZE=8m  \
	&& cd /img  \
	&& rm -rf XDS-INTEL64_Linux_x86_64.tar.gz
/bin/bash -c #(nop) COPY file:25abc9ade790f46c65d339108d9ee2dbaec929e33fefc82dd97108f07a39e222 in /img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6.tar.gz
	img/
	img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6.tar.gz

/bin/bash -c tar -xzvf phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6.tar.gz  \
	&& cd /img/phenix-installer-1.18.2-3874-intel-linux-2.6-x86_64-centos6  \
	&& ./install --prefix=/img/
```
