export interface Message {
  header: string;
  body: string;
  footer: string;
}

export interface Renderer {
  render(message: Message): string;
}
