import { useState } from "react";

import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
import ChatBox from "../components/ChatBox";
import ChatInput from "../components/ChatInput";

function Home() {

    const [selectedFile, setSelectedFile] = useState(null);

    const [uploaded, setUploaded] = useState(false);

    const [loading, setLoading] = useState(false);

    const [messages, setMessages] = useState([]);
    function clearChat() {

        setMessages([]);

    }

    return (

        <main className="min-h-screen bg-slate-100">

            <div className="max-w-6xl mx-auto px-6 py-10">

                <Navbar />

                <UploadBox
                    selectedFile={selectedFile}
                    setSelectedFile={setSelectedFile}
                    uploaded={uploaded}
                    setUploaded={setUploaded}
                    loading={loading}
                    setLoading={setLoading}
                />

                <ChatBox
                    messages={messages}
                    loading={loading}
                    clearChat={clearChat}
                />

                <ChatInput
                    uploaded={uploaded}
                    loading={loading}
                    setLoading={setLoading}
                    messages={messages}
                    setMessages={setMessages}
                />

            </div>

        </main>

    );

}

export default Home;