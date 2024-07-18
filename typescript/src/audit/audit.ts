import * as path from "path";
export interface FileSystem {
  getFiles: (directoryNAme: string) => string[];
  writeAllText: (newFile: string, content: string) => void;
  readAllLines: (path: string) => string[];
}
const fileSystem: () => FileSystem = () => {
  return {
    getFiles: () => {
      throw Error("not implemented");
    },
    writeAllText: (newFile: string, content: string) => {
      throw Error("not implemented");
    },
    readAllLines: (path: string) => {
      throw Error("not implemented");
    },
  };
};

interface AuditManager {
  addRecord(visitorName: string, timeOfVisit: Date): void;
}

export const createAuditManager = (
  maxEntriesPerFile: number,
  directoryName: string,
  fileSystem: FileSystem,
): AuditManager => {
  const _sortByIndex = (filePaths: string[]): [number, string][] => {
    return filePaths.map((filePath, index) => [index + 1, filePath]);
  };

  const addRecord = (visitorName: string, timeOfVisit: Date) => {
    const filePaths = fileSystem.getFiles(directoryName);
    const sortedPaths = _sortByIndex(filePaths);

    const newRecord = `${visitorName};${timeOfVisit.toLocaleString("en-US", { year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit" })}`;

    if (sortedPaths.length === 0) {
      const newFile = path.join(directoryName, "audit_1.txt");
      fileSystem.writeAllText(newFile, newRecord);
      return;
    }

    const [currentFileIndex, currFilePath] =
      sortedPaths[sortedPaths.length - 1];
    const lines = fileSystem.readAllLines(currFilePath);

    if (lines.length < maxEntriesPerFile) {
      lines.push(newRecord);
      const newContent = lines.join("\n");
      fileSystem.writeAllText(currFilePath, newContent);
    } else {
      const newIndex = currentFileIndex + 1;
      const newName = `audit_${newIndex}.txt`;
      const newFile = path.join(directoryName, newName);
      fileSystem.writeAllText(newFile, newRecord);
    }
  };

  return { addRecord };
};
