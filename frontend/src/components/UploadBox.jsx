import { useRef } from "react";

import { uploadPdf } from "../services/uploadApi";

function UploadBox({

    selectedFile,

    setSelectedFile,

    uploaded,

    setUploaded,

    loading,

    setLoading

}) {

    const fileInputRef = useRef(null);


    function handleFileChange(event) {

        const file = event.target.files[0];

        if (file) {

            setSelectedFile(file);

            setUploaded(false);

        }

    }


    async function handleUpload() {

        if (!selectedFile) return;

        try {

            setLoading(true);

            await uploadPdf(selectedFile);

            setUploaded(true);

            // alert("PDF uploaded successfully!");

        }

        catch (error) {

            console.error(error);

            alert("Failed to upload PDF.");

        }

        finally {

            setLoading(false);

        }

    }


    return (

        <section className="bg-white rounded-2xl shadow-lg border border-slate-200 p-10 mb-8">

            <h2 className="text-3xl font-bold text-slate-900">
                Upload PDF
            </h2>

            <p className="mt-2 text-lg font-medium text-slate-700">
                Choose a PDF to build your AI knowledge base.
            </p>


            <input

                type="file"

                accept=".pdf"

                ref={fileInputRef}

                onChange={handleFileChange}

                className="hidden"

            />


            <div className="mt-8 border-2 border-dashed border-slate-300 rounded-xl p-8 text-center">

                {

                    selectedFile ? (

                        <p className="text-xl font-semibold text-slate-800">

                            📄 {selectedFile.name}

                        </p>

                    ) : (

                        <p className="text-xl font-medium text-slate-500">

                            No PDF selected

                        </p>

                    )

                }

            </div>


            <div className="flex justify-center gap-5 mt-8">

                <button

                    onClick={() => fileInputRef.current.click()}
                    // disable the button when loading state  
                    disabled={loading}

                    className="px-8 py-3 rounded-xl bg-slate-200 hover:bg-slate-300 disabled:bg-slate-300 transition font-semibold text-lg"

                >

                    Choose PDF

                </button>


                <button

                    onClick={handleUpload}

                    disabled={!selectedFile || loading}

                    className={`px-8 py-3 rounded-xl text-white font-semibold text-lg transition

                    ${
                        selectedFile && !loading
                            ? "bg-blue-600 hover:bg-blue-700"
                            : "bg-slate-400 cursor-not-allowed"
                    }`}

                >

                    {

                        loading

                            ? "Uploading..."

                            : "Upload"

                    }

                </button>

            </div>


            <div className="mt-6 text-center">

                {

                    uploaded && (

                        <p className="text-green-600 font-semibold text-lg">

                            ✓ PDF uploaded successfully

                        </p>

                    )

                }

            </div>

        </section>

    );

}

export default UploadBox;