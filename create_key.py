# /usr/bin/python3.6

import boto3

ec2 = boto3.resource('ec2')


def createKey():
    print("Creating a Key\n")
    outfile = open('ec2-keypair.pem', 'w')

    key_pair = ec2.create_key_pair(KeyName='ec2-keypair')

    KeyPairOut = str(key_pair.key_material)
    print(KeyPairOut)
    outfile.write(KeyPairOut)


def main():
    createKey()


if __name__ == '__main__':
    main()