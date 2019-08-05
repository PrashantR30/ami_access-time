# /usr/bin/python3.6

import boto3, json, time, datetime

ec2 = boto3.resource('ec2')


def createInstance(imageId):
    startTime = time.time()
    svalue = datetime.datetime.fromtimestamp(startTime)
    print("Started at ", svalue.strftime('%Y-%m-%d %H:%M:%S'))

    instance = ec2.create_instances(ImageId=imageId,
                                    MinCount=1,
                                    MaxCount=1,
                                    InstanceType='m4.xlarge',
                                    KeyName='ec2-keypair')

    print(instance)
    status = (instance[0].state['Name'])

    # id = instance[0].id

    while status != 'running':
        time.sleep(0.001)
        status = (instance[0].state['Name'])
        instance[0].load()

    endTime = time.time()
    evalue = datetime.datetime.fromtimestamp(endTime)
    print("Ended at ", evalue.strftime('%Y-%m-%d %H:%M:%S'))

    t = endTime - startTime
    seconds = t % 60
    print("TimeTaken to create Instance= ", seconds)
    print(instance[0].instance_type)
    print(instance[0].public_ip_address)


def main():

    desc = "Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type - ami-0fb6b6f9e81056553"
    imageId = 'ami-0fb6b6f9e81056553'

    # desc = "Amazon Linux 2 AMI (HVM), SSD Volume Type - ami-01f7527546b557442"
    # imageId = 'ami-01f7527546b557442'

    print(desc)
    print(imageId)

    createInstance(imageId)


if __name__ == '__main__':
    main()