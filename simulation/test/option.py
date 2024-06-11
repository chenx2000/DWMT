import argparse
import template

parser = argparse.ArgumentParser(description="Dual-Window Multiscale Transformer")
parser.add_argument('--template', default='dwmt', help='You can set various templates in option.py')

# Hardware specifications
parser.add_argument("--gpu_id", type=str, default='6')

# Data specifications
parser.add_argument('--data_root', type=str, default='../../datasets/', help='dataset directory')

# Saving specifications
parser.add_argument('--outf', type=str, default='./exp/dwmt/', help='saving_path')

# Model specifications
parser.add_argument('--method', type=str, default='dwmt', help='method name')
parser.add_argument('--pretrained_model_path', type=str, default=None, help='pretrained model directory')
parser.add_argument("--input_setting", type=str, default='H', help='the input measurement of the network: H, HM or Y')
parser.add_argument("--input_mask", type=str, default='Mask',
                    help='the input mask of the network: Phi, Phi_PhiPhiT, Mask or None')  # Phi: shift_mask, Mask: mask

opt = parser.parse_args()
template.set_template(opt)

opt.mask_path = f"{opt.data_root}/TSA_simu_data/"
opt.test_path = f"{opt.data_root}/TSA_simu_data/Truth/"

for arg in vars(opt):
    if vars(opt)[arg] == 'True':
        vars(opt)[arg] = True
    elif vars(opt)[arg] == 'False':
        vars(opt)[arg] = False