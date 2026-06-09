import { useState } from "react";
import API from "../services/api";

function UploadSection({ onUploadSuccess }) {

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {

    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {

      setLoading(true);

      await API.post(
        "/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      );

      onUploadSuccess();

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }

  };

  return (
    <div>

      <h2>Upload Dataset</h2>

      <input
        type="file"
        accept=".csv"
        onChange={(e) =>
          setFile(e.target.files[0])
        }
      />

      <br />
      <br />

      <button onClick={handleUpload}>
        {loading ? "Uploading..." : "Upload CSV"}
      </button>

    </div>
  );
}

export default UploadSection;