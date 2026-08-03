resource "google_artifact_registry_repository" "app" {
  depends_on = [google_project_service.required_apis]

  project       = var.project_id
  location      = var.region
  repository_id = "cloud-sql-provisioner"
  format        = "DOCKER"
}