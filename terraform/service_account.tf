resource "google_service_account" "sa_cloudsql" {
  account_id   = "sa-cloud-sql-provider"
  display_name = "sa-cloudsql"
  description  = "Service Account para se comunicar com a API do Cloud SQL"
  project      = var.project_id
}

resource "google_project_iam_member" "cloudsql_admin_permission" {
  depends_on = [google_service_account.sa_cloudsql]
  project    = var.project_id
  role       = "roles/cloudsql.admin"
  member     = "serviceAccount:${google_service_account.sa_cloudsql.email}"
}

