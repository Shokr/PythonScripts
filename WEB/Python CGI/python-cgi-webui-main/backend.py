#!/usr/bin/python3
import cgi
import subprocess as sp

print("content-type: text/html")
print()

data = cgi.FieldStorage()
a = data.getvalue("a")

if a == "linux-1":
    x = data.getvalue("x")
    output = sp.getoutput("mkdir {}".format(x))
elif a == "linux-2":
    output = sp.getoutput("ls")
    print()
    print(output)
elif a == "linux-3":
    x = data.getvalue("x")
    output = sp.getoutput("touch {}".format(x))
elif a == "linux-4":
    x = data.getvalue("x")
    output = sp.getoutput("cat {}".format(x))
elif a == "linux-5":
    x = data.getvalue("x")
    output = sp.getoutput("useradd {}".format(x))
    print(output)
elif a == "linux-6":
    x = data.getvalue("x")
    output = sp.getoutput("passwd {}".format(x))
    print(output)
elif a == "linux-7":
    output = sp.getoutput("free -m")
    print(output)
elif a == "linux-8":
    output = sp.getoutput("df -hT")
    print(output)
elif a == "linux-9":
    x = data.getvalue("x")
    output = sp.getoutput("rpm -q {}".format(x))
    print(output)
elif a == "linux-10":
    x = data.getvalue("x")
    output = sp.getoutput("rpm -e {}".format(x))
    print(output)
elif a == "linux-11":
    output = sp.getoutput("ifconfig enp0s3")
    print(output)
elif a == "linux-12":
    output = sp.getoutput("jps")
    print(output)
elif a == "linux-13":
    output = sp.getoutput("lscpu")
    print(output)
elif a == "linux-14":
    output = sp.getoutput("ps -aux")
    print(output)
elif a == "linux-15":
    output = sp.getoutput("uptime")
    print(output)
elif a == "linux-16":
    output = sp.getoutput("echo 3 > /proc/sys/vm/drop_caches")
    print(output)
elif a == "linux-17":
    x = data.getvalue("x")
    output = sp.getoutput("yum whatprovides {}".format(x))
    print(output)
elif a == "linux-18":
    x = data.getvalue("x")
    output = sp.getoutput("ping {}".format(x))
    print(output)
elif a == "linux-19":
    x = data.getvalue("x")
    y = data.getvalue("y")
    output = sp.getoutput("useradd -s {} {}".format(x, y))
    print(output)
elif a == "linux-20":
    x = data.getvalue("x")
    output = sp.getoutput("date")
    print(output)
elif a == "aws-1":
    output = sp.getoutput("aws configure")
    print(output)
elif a == "aws-2":
    x = data.getvalue("x")
    output = sp.getoutput("aws ec2 create-key-pair --key-name {}".format(x))
    print(output)
elif a == "aws-3":
    x = data.getvalue("x")
    output = sp.getoutput("aws ec2 create-security-group --group-name {}".format(x))
    print(output)
elif a == "aws-4":
    x = data.getvalue("x")
    y = data.getvalue("y")
    z = data.getvalue("z")
    b = data.getvalue("b")
    c = data.getvalue("c")
    d = data.getvalue("d")
    output = sp.getoutput(
        "aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --key-name {} --security-group-ids {}".format(
            x, y, z, b, c, d
        )
    )
    print(output)
elif a == "aws-5":
    x = data.getvalue("x")
    y = data.getvalue("y")
    output = sp.getoutput(
        "aws ec2 create-volume --availability-zone {} --no-encrypted --size {}".format(
            x, y
        )
    )
    print(output)
elif a == "aws-6":
    x = data.getvalue("x")
    y = data.getvalue("y")
    output = sp.getoutput(
        "aws ec2 attach-volume --instance-id {} --volume-id {} --device xvdh".format(
            x, y
        )
    )
    print(output)
elif a == "aws-7":
    x = data.getvalue("x")
    y = data.getvalue("y")
    output = sp.getoutput(
        "aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(
            x, y, y
        )
    )
    print(output)
elif a == "docker-1":
    output = sp.getoutput("docker -version")
    print(output)
elif a == "docker-2":
    x = data.getvalue("x")
    y = data.getvalue("y")
    output = sp.getoutput("docker run -dit --name {}  {}".format(x, y))
    print(output)
elif a == "docker-3":
    x = data.getvalue("x")
    # y = data.getvalue('y')
    output = sp.getoutput("docker pull {}".format(x))
    print(output)
elif a == "docker-4":
    # y = data.getvalue('y')
    output = sp.getoutput("docker ps")
    print(output)
elif a == "docker-5":
    # y = data.getvalue('y')
    output = sp.getoutput("docker ps -a")
    print(output)
elif a == "docker-6":
    # y = data.getvalue('y')
    output = sp.getoutput("docker images")
    print(output)
elif a == "docker-7":
    x = data.getvalue("x")
    # y = data.getvalue('y')
    output = sp.getoutput("docker start {}".format(x))
    print(output)
elif a == "docker-8":
    x = data.getvalue("x")
    # y = data.getvalue('y')
    output = sp.getoutput("docker stop {}".format(x))
    print(output)
elif a == "docker-9":
    x = data.getvalue("x")
    # y = data.getvalue('y')
    output = sp.getoutput("docker rm {}".format(x))
    print(output)
elif a == "docker-10":
    # y = data.getvalue('y')
    output = sp.getoutput("docker stop $(docker ps -aq)")
    print(output)
elif a == "docker-11":
    # y = data.getvalue('y')
    output = sp.getoutput("docker rm $(docker ps -aq)")
    print(output)
elif a == "hadoop-1":
    # y = data.getvalue('y')
    output = sp.getoutput("hadoop version")
    print(output)
elif a == "hadoop-2":
    # y = data.getvalue('y')
    output = sp.getoutput("hadoop namenode -format")
    print(output)
elif a == "hadoop-3":
    # y = data.getvalue('y')
    output = sp.getoutput("hadoop-daemon.sh start namenode")
    print(output)
elif a == "hadoop-4":
    # y = data.getvalue('y')
    output = sp.getoutput("hadoop-daemon.sh start datanode")
    print(output)
elif a == "hadoop-5":
    # y = data.getvalue('y')
    output = sp.getoutput("hadoop dfsadmin -report")
    print(output)
elif a == "hadoop-6":
    # y = data.getvalue('y')
    output = sp.getoutput("hadoop fs -ls /")
    print(output)
elif a == "hadoop-7":
    x = data.getvalue("x")
    y = data.getvalue("y")
    output = sp.getoutput("hadoop fs -put {}/{}".format(x, y))
    print(output)
elif a == "hadoop-8":
    x = data.getvalue("x")
    # y = data.getvalue('y')
    output = sp.getoutput("hadoop fs -rm /{}".format(x))
    print(output)
elif a == "hadoop-9":
    x = data.getvalue("x")
    # y = data.getvalue('y')
    output = sp.getoutput("hadoop fs -cat /{}".format(x))
    print(output)
elif a == "hadoop-10":
    x = data.getvalue("x")
    y = data.getvalue("y")
    output = sp.getoutput("hadoop fs -Ddfs.block.size={}  -put {} /".format(x, y))
    print(output)
elif a == "hadoop-11":
    x = data.getvalue("x")
    # y = data.getvalue('y')
    output = sp.getoutput("hadoop fs -touchz {} /".format(x))
    print(output)
