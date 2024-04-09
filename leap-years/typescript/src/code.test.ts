import { magicNumberGenerator } from "./code";

describe("test", () => {
  it("should test the magic number", () => {
    const magicNumber = magicNumberGenerator();
    expect(magicNumber).toBe(47);
  });
});
