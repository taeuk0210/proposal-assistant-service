export type ChatRequest = {
  message: string
}

export type ChatContent = {
  roleType: "assistant" | "user"
  message: string
}