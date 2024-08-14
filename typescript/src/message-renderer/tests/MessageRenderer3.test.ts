import { MessageRenderer } from "../message-renderer";
import { Message } from "../renderer.model";

describe("MessageRenderer", () => {
  test("message_renderer", () => {
    const sut = new MessageRenderer();
    const message: Message = {
      header: "h",
      body: "b",
      footer: "f",
    };
    const html = sut.render(message);
    expect(html).toBe("<h1>h</h1><b>b</b><i>f</i>");
  });
});
