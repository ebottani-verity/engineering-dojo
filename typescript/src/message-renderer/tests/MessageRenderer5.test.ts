import { MessageRenderer } from "../message-renderer";

describe("MessageRenderer", () => {
  test("message_renderer", () => {
    const sut = new MessageRenderer();

    const renderers = sut.getSubRenderers();

    expect(sut).not.toBeNull();
    expect(renderers).not.toBeNull();
  });
});
