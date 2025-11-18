import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { toast } from "sonner";

export default function Unload() {
  const [files, setFiles] = useState<string[]>([]);
  const [selected, setSelected] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectAll, setSelectAll] = useState(false);

  const fetchFiles = async () => {
    const res = await fetch("http://localhost:5000/api/uploads/list");
    const data = await res.json();
    setFiles(data.files);
    setLoading(false);
  };

  useEffect(() => {
    fetchFiles();
  }, []);

  const toggleSelect = (file: string) => {
    setSelected((prev) =>
      prev.includes(file) ? prev.filter((f) => f !== file) : [...prev, file]
    );
  };

  const toggleSelectAll = () => {
    if (!selectAll) setSelected(files);
    else setSelected([]);
    setSelectAll(!selectAll);
  };

  const deleteFiles = async () => {
    if (selected.length === 0) {
      toast.error("Select at least one file to delete");
      return;
    }

    const res = await fetch("http://localhost:5000/api/uploads/delete", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ files: selected }),
    });

    const data = await res.json();
    toast.success(data.message);

    setSelected([]);
    setSelectAll(false);
    fetchFiles();

    localStorage.setItem("triggerRefresh", Date.now().toString());
  };

  return (
    <div className="p-8">

      {/* Page Title + Delete Button (TOP-RIGHT) */}
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-3xl font-bold">Unload / Remove PDFs</h1>

        <Button
          onClick={deleteFiles}
          className="bg-red-600 text-white"
          disabled={selected.length === 0}
        >
          Delete Selected PDFs ({selected.length})
        </Button>
      </div>

      <Card className="p-6">
        {loading ? (
          <p>Loading...</p>
        ) : files.length === 0 ? (
          <p>No PDFs uploaded today.</p>
        ) : (
          <div className="space-y-3">

            {/* Select All */}
            <div className="flex items-center justify-between p-2 border rounded bg-accent/10">
              <label className="flex items-center gap-2 font-semibold">
                <input
                  type="checkbox"
                  checked={selectAll}
                  onChange={toggleSelectAll}
                />
                Select All PDFs
              </label>

              <span className="text-sm text-muted-foreground">
                Selected: <b>{selected.length}</b> / {files.length}
              </span>
            </div>

            {/* File List */}
            {files.map((file) => (
              <div
                key={file}
                className="flex items-center justify-between p-2 border rounded hover:bg-accent/20 transition"
              >
                <label className="flex items-center gap-2">
                  <input
                    type="checkbox"
                    checked={selected.includes(file)}
                    onChange={() => toggleSelect(file)}
                  />
                  {file}
                </label>
              </div>
            ))}
          </div>
        )}
      </Card>
    </div>
  );
}
