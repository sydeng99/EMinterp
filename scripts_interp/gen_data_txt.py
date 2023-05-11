import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--folder', type=str, help='path to training data')
args = parser.parse_args()

txt=open(args.folder+'/train_data.txt', 'w')
num = len(os.listdir(args.folder))
for i in range(num):
    txt.write('train_data/'+str(i).zfill(4)+'_1.png' + ' ' +'train_data/'+str(i).zfill(4)+'_2.png' + ' ' +'train_data/'+ str(i).zfill(4)+'_3.png' + '\n')
txt.close()