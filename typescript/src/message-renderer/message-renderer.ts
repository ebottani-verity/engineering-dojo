import { Message, Renderer } from "./renderer.model";
import { HeaderRenderer } from "./header-renderer";
import { BodyRenderer } from "./body-renderer";
import { FooterRenderer } from "./footer-renderer";

export class MessageRenderer implements Renderer {
  private subRenderers: Renderer[];

  constructor() {
    this.subRenderers = [
      new HeaderRenderer(),
      new BodyRenderer(),
      new FooterRenderer(),
    ];
  }

  public getSubRenderers(): Renderer[] {
    return this.subRenderers;
  }

  public render(message: Message): string {
    return this.subRenderers
      .map((renderer) => renderer.render(message))
      .reduce((acc, renderedPart) => acc + renderedPart, "");
  }
}
