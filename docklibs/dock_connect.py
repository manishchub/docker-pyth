# Connection to GCP VM
import googleapiclient.discovery
compute = googleapiclient.discovery.build('compute', 'v1')

