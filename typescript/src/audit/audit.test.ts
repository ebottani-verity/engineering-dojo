import { createAuditManager } from "./audit";

interface MockFileSystem {
  getFiles(directoryName: string): string[];
  readAllLines(filePath: string): string[];
  writeAllText(filePath: string, content: string): void;
}

describe("AuditManager", () => {
  it("creates a new file when the current file overflows", () => {
    const mockFileSystem: MockFileSystem = {
      getFiles(directoryName: string): string[] {
        return ["audits/audit_2.txt", "audits/audit_1.txt"];
      },
      readAllLines(filePath: string): string[] {
        return [
          "Peter;04/06/2019, 04:30:00 PM",
          "Jane;04/06/2019, 04:40:00 PM",
          "Jack;2019-04-06 17:00:00",
        ];
      },
      writeAllText(filePath: string, content: string): void {
        // No implementation needed for the test
      },
    };

    const writeAllTextSpy = jest.spyOn(mockFileSystem, "writeAllText");

    const auditManager = createAuditManager(3, "audits", mockFileSystem);

    auditManager.addRecord(
      "Alice",
      new Date(Date.parse("2019-04-06T18:00:00")),
    );

    expect(writeAllTextSpy).toHaveBeenCalledWith(
      "audits/audit_3.txt",
      "Alice;04/06/2019, 06:00:00 PM",
    );
  });
});
