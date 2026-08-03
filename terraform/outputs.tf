output "service_account_email" {
  value = google_service_account.sa_cloudsql.email
}

output "gke_cluster_name" {
  value = google_container_cluster.cloudsql_provisioner.name
}
