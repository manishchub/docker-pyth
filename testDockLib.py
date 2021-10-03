import docklibs

from docklibs import dock_control
from docklibs.dock_control import *

client=dock_login()
images=dock_get_images(client)


#cont=create_containers(client,'nginx:1.15')
#print("Name:"+cont.attrs['Name'] + " "+"Id:"+cont.attrs['Id']+" " + "Status:" + " " + cont.attrs['State']['Status'])

#stop_container(client,cont)
#print("Name:"+cont.attrs['Name'] + " "+"Id:"+cont.attrs['Id']+" " + "Status:" + " " + cont.attrs['State']['Status'])

get_all_images(client)

current_ver_containers=get_all_containers(client,images[2])
# for cont in current_ver_containers:
#     stop_container(client,cont)

# client.containers.prune()
#print(current_ver_containers)

print(deploy_rollout(client,images[2],images[1]))
