variable "project_id" {
  type = string
}

variable "region" {
  type = string
}

variable "user" {
  type = string
}

variable "gke_cluster_name" {
  type    = string
  default = "cloud-sql-provisioner-cluster"
}

variable "k8s_namespace" {
  type    = string
  default = "default"
}

variable "k8s_ksa_name" {
  type    = string
  default = "cloud-sql-provisioner"
}