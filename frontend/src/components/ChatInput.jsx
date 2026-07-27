import { useState } from "react";
import { FiSend } from "react-icons/fi";

import { askQuestion } from "../services/chatApi";

function ChatInput({

    uploaded,

    loading,

    setLoading,

    messages,

    setMessages

}) {

    const [question, setQuestion] = useState("");


    async function handleSend() {

        if (!question.trim()) return;


        const userMessage = {
            role: "user",
            text: question
        };


        setMessages((previous) => [

            ...previous,

            userMessage

        ]);


        const currentQuestion = question;

        setQuestion("");


        try {

            setLoading(true);

            const response = await askQuestion(currentQuestion);
            console.log(response);
            const assistantMessage = {

                role: "assistant",

                text: response.answer,

                confidence: response.confidence,

                youtube: response.youtube,

                web: response.web

            };


            setMessages((previous) => [

                ...previous,

                assistantMessage

            ]);

        }

        catch (error) {

            console.error(error);

            setMessages((previous) => [

                ...previous,

                {

                    role: "assistant",

                    text: "Sorry, something went wrong."

                }

            ]);

        }

        finally {

            setLoading(false);

        }

    }


    function handleKeyDown(event) {

        if (

            event.key === "Enter" &&

            !event.shiftKey

        ) {

            event.preventDefault();

            handleSend();

        }

    }


    return (

        <section className="bg-white rounded-2xl shadow-lg border border-slate-200 p-5">

            <div className="flex items-center gap-4">

                <textarea

                    rows="2"

                    value={question}

                    onChange={(event) =>

                        setQuestion(event.target.value)

                    }

                    onKeyDown={handleKeyDown}

                    disabled={!uploaded || loading}

                    placeholder={

                        uploaded

                            ? "Ask a question about your PDF..."

                            : "Upload a PDF first..."

                    }

                    className="flex-1 resize-none outline-none text-lg text-slate-700 placeholder:text-slate-400"

                />


                <button

                    onClick={handleSend}

                    disabled={

                        !uploaded ||

                        loading ||

                        !question.trim()

                    }

                    className={`

                        w-14 h-14 rounded-xl

                        flex items-center justify-center

                        transition

                        ${

                            uploaded &&

                            question.trim() &&

                            !loading

                                ? "bg-blue-600 hover:bg-blue-700 text-white"

                                : "bg-slate-300 text-slate-500 cursor-not-allowed"

                        }

                    `}

                >

                    <FiSend size={24} />

                </button>

            </div>

        </section>

    );

}

export default ChatInput;