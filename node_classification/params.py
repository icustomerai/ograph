import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Model Parameters')
    parser.add_argument('--lr', default=1e-4, type=float, help='learning rate')
    parser.add_argument('--batch', default=1024, type=int, help='training batch size')
    parser.add_argument('--tst_batch', default=256, type=int, help='testing batch size (number of users)')
    parser.add_argument('--shot', default=-1, type=int, help='number of shots for each node')
    parser.add_argument('--epoch', default=50, type=int, help='number of epochs')
    parser.add_argument('--tune_step', default=100, type=int, help='number of projection tuning steps')
    parser.add_argument('--save_path', default='tem', help='file name to save model and training record')
    parser.add_argument('--load_model', default=None, help='model name to load')
    parser.add_argument('--tstdata', default='', type=str, help='name of test dataset')
    parser.add_argument('--tst_epoch', default=1, type=int, help='number of epoch to test while training')
    parser.add_argument('--gpu', default='0', type=str, help='indicates which gpu to use')
    parser.add_argument('--topk', default=20, type=int, help='topk in evaluation')
    parser.add_argument('--cache_adj', default=0, type=int, help='indicates wheter cache bidirectional adjs')
    parser.add_argument('--cache_proj', default=1, type=int, help='indicates wheter cache projector and matrices')
    parser.add_argument('--epoch_max_step', default=-1, type=int, help='indicates the maximum number of steps in one epoch, -1 denotes full steps')
    parser.add_argument('--data_dir', default='../datasets', type=str, help='dataset directory')

    parser.add_argument('--niter', default=2, type=int, help='number of iteration in svd')
    parser.add_argument('--reg', default=1e-7, type=float, help='weight decay regularizer')
    parser.add_argument('--drop_rate', default=0.1, type=float, help='dropout rate')
    parser.add_argument('--scale_layer', default=10, type=float, help='per-layer scale factor')
    parser.add_argument('--clamp', default=-1, type=float, help='absolute value for the limit of prediction scores while training')
    parser.add_argument('--mask_method', default='trn', type=str, help='which graph masking method to use')
    parser.add_argument('--mask_alg', default='linear', type=str, help='which graph masking algorithm in trn mask_method')
    parser.add_argument('--random_mask_rate', default=0.5, type=float, help='mask ratio in random mask_method')
    parser.add_argument('--act', default='leaky', type=str, help='activation function')
    parser.add_argument('--leaky', default=0.5, type=float, help='slope of leaky relu activation')
    parser.add_argument('--latdim', default=1024, type=int, help='latent dimensionality')
    parser.add_argument('--head', default=4, type=int, help='number of attention heads')
    parser.add_argument('--selfloop', default=0, type=int, help='indicating using self-loop or not')
    parser.add_argument('--gnn_layer', default=3, type=int, help='number of gnn iterations')
    parser.add_argument('--gt_layer', default=4, type=int, help='number of graph transformer layers')
    parser.add_argument('--proj_method', default='svd', type=str, help='initial projection method')
    parser.add_argument('--mask', default='trn', type=str, help='indicating which mask strategy to apply')
    parser.add_argument('--loss', default='ce', type=str, help='loss function')
    parser.add_argument('--mask_bat', default=512, type=int, help='batch size for masking')
    parser.add_argument('--anchor', default=256, type=int, help='number of anchor nodes in the compressed graph transformer')
    parser.add_argument('--pred_iter', default=1, type=int, help='number of prediction iterations')
    parser.add_argument('--proj_trn_steps', default=10, type=int, help='number of training steps for one initial projection')
    return parser.parse_args()
args = parse_args()