import { Message, Renderer } from "./renderer.model";

export class BodyRenderer implements Renderer {
  render(message: Message): string {
    return `<b>${message.body}</b>`;
  }
}
