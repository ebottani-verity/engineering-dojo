import { Message, Renderer } from "./renderer.model";

export class HeaderRenderer implements Renderer {
  render(message: Message): string {
    return `<h1>${message.header}</h1>`;
  }
}
