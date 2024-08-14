import { readFileSync } from "fs";
import { join } from "path";
import { Message } from "../renderer.model";
import { MessageRenderer } from "../message-renderer";

describe("MessageRenderer", () => {
  test("message_renderer", () => {
    const location = process.cwd();
    const filePath = join(location, "src", "message-renderer", "resources");
    const header = readFileSync(join(filePath, "header.txt"), "utf-8");
    const body = readFileSync(join(filePath, "body.txt"), "utf-8");
    const footer = readFileSync(join(filePath, "footer.txt"), "utf-8");

    const message: Message = {
      header: header.trim(),
      body: body.trim(),
      footer: footer.trim(),
    };

    const sut = new MessageRenderer();
    const html = sut.render(message);

    expect(html.startsWith("<h1>Lorem ipsum dolor sit amet")).toBe(true);
    expect(html.endsWith("doloribus asperiores repellat.</i>")).toBe(true);
  });
});
