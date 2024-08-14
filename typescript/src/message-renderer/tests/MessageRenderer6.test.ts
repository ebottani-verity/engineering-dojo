import { Message } from "../renderer.model";
import { MessageRenderer } from "../message-renderer";

describe("MessageRenderer", () => {
  test("message_renderer", () => {
    const message: Message = {
      header: "header",
      body: "body",
      footer: "footer",
    };
    const sut = new MessageRenderer();

    const html = sut.render(message);

    expect(html).toMatchSnapshot();
  });
});
