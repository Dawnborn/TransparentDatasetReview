# TransparentDatasetReview

Here we collected the existing datsets containing transparent/translucent objects and their models (if available)

| Dataset | Mesh File | Modality | Scale |Extrinsics / Traj | Comments |
|----------|----------|----------|----------|----------|----------|
| [TransCG (2022RAL)](https://github.com/Galaxies99/TransCG) | Scanned | RGBD | 57k images of 130 scenes | stereo pairs, relative poses of objects |
| [ClearGrasp (2019)](https://sites.google.com/view/cleargrasp/home) | Synthetic (not public) | RGBD. normal, segmentation | 50k images synthetic + 286 images real-world | mono images, relative poses of objects |
| [Dex-NeRF Datasets (CoRL 2021)](https://sites.google.com/view/dex-nerf) | Not Available | RGB | 400~ images (2 synthetic scenes and 2 real-world scenes) | Relative poses of objects |
| [TransparentShapeRealData (CVPR 2020)](https://github.com/yuyingyeh/TransparentShapeRealData) | Scanned to Synthetic (optix renderer) | RGB, normal | 4 scenes with creation pipeline |  |
| [KeyPose Dataset (CVPR 2020)](https://sites.google.com/view/keypose/?pli=1) | Scanned | RGBD | 48k images, 15 scenes | Stereo sequences, relative pose of objects|
| [TransProteus (2021)](https://www.cs.toronto.edu/matterlab/TransProteus/) | Synthetic (Partly from ShapeNet with given BRDFs) | RGBD | 50k images, 13000 objects | Fixed Angles, incomplete scene file|
| [ClearPose (ECCV 2022)](https://github.com/opipari/ClearPose) | Synthetic (available, alligned with real images) | RGBD, normal | 350k images, 63 objects | Sparse viewpoints with relative poses of objects |
| [Omniverse Object Dataset (CVPR 2021)](https://github.com/NVlabs/implicit_depth) | Synthetic | RGBD, transparent mask | 60k images | Sparse mono viewpoints with camera extrinsics|
| [SuperCaustics (2021)](https://github.com/MMehdiMousavi/SuperCaustics) | Synthetic (Mesh provided in UE4 project) | RGB, Depth (Not available), normal (Not available) | 9k images, 650 scenarios | Sparse viewpoints, mono, no extrinsics or poses given, might be in the project |
| [Trans10K (ECCV 2020)](https://github.com/xieenze/Segment_Transparent_Objects) | Not Available | RGB, Segmentation | 10k images |  | only for 2D segmentation |
| [DRT (TOG 2020)](https://github.com/lvjiahui/DRT) | Scanned (Grey code) | 3D mesh to be rendered | 8 models, images can be rendered |  | #TODO 3D to 3D metrics |
| [DREDS dataset (ECCV 2022)](https://github.com/PKU-EPIC/DREDS#dataset) | Synthetic | RGBD | 130k images, 1801 scenes. |  | #TODO |
| [GraspNeRF (2023ICRA)](https://github.com/PKU-EPIC/GraspNeRF) | Synthetic | RGB | 2.4 million images of 100K scenes | | #TODO generation pipeline with Blender assets, based on DREDS |
| [TransPIR (2022)](https://github.com/shaomq2187/transpir) | Synthetic | RGB, normal | 1k images, 4 models |  |