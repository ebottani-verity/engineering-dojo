import { Message, Renderer } from "./renderer.model";

export class FooterRenderer implements Renderer {
  render(message: Message): string {
    return `<i>${message.footer}</i>`;
  }
}
