import { MessageRenderer } from "../message-renderer";
import { HeaderRenderer } from "../header-renderer";
import { BodyRenderer } from "../body-renderer";
import { FooterRenderer } from "../footer-renderer";

describe("MessageRenderer", () => {
  test("message_renderer", () => {
    const sut = new MessageRenderer();

    const renderers = sut.getSubRenderers();
    expect(renderers.length).toBe(3);
    expect(renderers[0]).toBeInstanceOf(HeaderRenderer);
    expect(renderers[1]).toBeInstanceOf(BodyRenderer);
    expect(renderers[2]).toBeInstanceOf(FooterRenderer);
  });
});
