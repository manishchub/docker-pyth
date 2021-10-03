#docker login
import docker
from time import sleep

def dock_login():
    client = docker.from_env()
    client.login(username='montish',password='Docker@2019',registry='https://index.docker.io/v1/')

    return client

def dock_get_images(client):
    image_list=client.images.list()
    image_list_ver=[]

    for images in image_list:
        image_name=tuple(str(images).split(":"))
        image_ver=(image_name[1].replace("'","")+":"+image_name[2].replace(">","").replace("'",""))
        image_list_ver.append(image_ver.strip())
    print(image_list_ver)
    return image_list_ver

def create_containers(client,img):

    print("Creating container for image " + img)
    container=client.containers.run(image=img,detach=True)

    timeout = 20
    stop_time = 5
    elapsed_time = 0
    while container.status != 'running' and elapsed_time < timeout:
        sleep(stop_time)
        elapsed_time += stop_time
        container.reload()
        continue
    container.reload()
    return container

def get_cont_status(cont):
    return cont.attrs['State']['Status']

def stop_container(client,cont):
    print("Container ID to be stopped is " + cont.id)
    #cont_obj=client.containers.get(cont.id)
    # cont_obj.stop()
    # cont_obj.wait()
    cont.stop()
    cont.wait()
    cont.reload()
    print("Stop Container status is.. " + get_cont_status(cont))

    if get_cont_status(cont)=="exited":
        print("Container " + cont.id + " has been stopped...")
        cont.reload()
        return True
    else:
        cont.reload()
        return False

def get_all_images(client):

    image_list=client.images.list()
    image_list_ver=[]
    for images in image_list:
      image_name=tuple(str(images).split(":"))
      image_ver=(image_name[1].replace("'","")+":"+image_name[2].replace(">","").replace("'",""))
      image_list_ver.append(image_ver.strip())
    print("Image List " + str(image_list_ver))
    return True

# def deploy_rollout(client,old_image_ver,new_image_ver):
#     # stop old version container and confirm its status
#
#
#
#     # start new version container and confirm its status


def get_all_containers(client, image_ver):
    image_container_list=client.containers.list(all=True,filters={'status':'running','ancestor':image_ver})
    print(len(image_container_list))
    return image_container_list

def deploy_rollout(client,old_image_ver,new_image_ver):

    #get list of containers for old_image
    old_container_list=get_all_containers(client, old_image_ver)
    old_container_count=len(old_container_list)
    new_list=[]
    old_list=[]


    for cont in old_container_list:
        #create new version container and confirm its status
        new_list.append(create_containers(client,new_image_ver))

        #stop old version container and confirm its status
        old_list.append(cont)
        stop_container(client,cont)

    return old_list,new_list
