resource "google_container_cluster" "cloudsql_provisioner" {
  depends_on = [google_project_service.required_apis]

  name     = var.gke_cluster_name
  project  = var.project_id
  location = var.region

  enable_autopilot    = true
  deletion_protection = false
}
