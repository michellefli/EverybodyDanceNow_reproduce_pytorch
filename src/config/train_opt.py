batchSize=1
beta1=0.5
checkpoints_dir='./checkpoints/'
continue_train=False
data_type=32
dataroot='./data/target/train'
load_pretrain = './checkpoints/target/' # CHANGE: USING! use this if you want to continue last training
debug=False
display_freq=640
display_winsize=512
feat_num=3
fineSize=512
fine_size=480
input_nc=3
instance_feat=False
isTrain=True
label_feat=False
label_nc=18
lambda_feat=10.0
loadSize=512
load_features=False
load_pretrain='' 
lr=0.0002
max_dataset_size=100000
model='pix2pixHD'
nThreads=2
n_blocks_global=9
n_blocks_local=3
n_clusters=10
n_downsample_E=4
n_downsample_global=4
n_layers_D=3
n_local_enhancers=1
name='target'
ndf=64
nef=16
netG='global'
ngf=64
niter=1  # CHANGE from 20
niter_decay=0  # CHANGE from 20
niter_fix_global=0
no_flip=False
no_ganFeat_loss=False
no_html=False
no_instance=True
no_lsgan=False
no_vgg_loss=False
norm='instance'
num_D=2
output_nc=3
phase='train'
pool_size=0
print_freq=640
resize_or_crop='scale_width'
save_epoch_freq=10
save_latest_freq=640
serial_batches=False
tf_log=True
use_dropout=False
verbose=False
which_epoch='latest'
gpu_ids=[0]