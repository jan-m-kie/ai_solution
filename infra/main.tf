provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "ai_solution" {
  metadata {
    name = "ai-solution"
  }
}

output "namespace" {
  value = kubernetes_namespace.ai_solution.metadata[0].name
}