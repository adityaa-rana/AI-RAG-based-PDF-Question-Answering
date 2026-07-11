import { useState } from "react";
import { FiCopy } from "react-icons/fi";

function Message({

    role,

    text,

    confidence

}) {

    const isUser = role === "user";

    const [copied, setCopied] = useState(false);

    async function handleCopy() {

        await navigator.clipboard.writeText(text);

        setCopied(true);

        setTimeout(() => {

            setCopied(false);

        }, 2000);

    }

    return (

        <div className="mb-8">

            <div className="flex items-center justify-between mb-3">

                <div className="flex items-center gap-3">

                    <div
                        className={`w-10 h-10 rounded-full flex items-center justify-center text-white font-bold
                        ${
                            isUser
                                ? "bg-slate-700"
                                : "bg-blue-600"
                        }`}
                    >
                        {isUser ? "U" : "AI"}
                    </div>

                    <h3 className="text-xl font-bold text-slate-800">

                        {isUser ? "You" : "Assistant"}

                    </h3>

                </div>

                {
                    !isUser && (

                        <button
                            onClick={handleCopy}
                            className="flex items-center gap-2 text-slate-500 hover:text-blue-600 transition"
                        >

                            <FiCopy size={16} />

                            {
                                copied
                                    ? "Copied!"
                                    : "Copy"
                            }

                        </button>

                    )
                }

            </div>

            <div
                className="ml-13 text-lg leading-8 text-slate-700 whitespace-pre-wrap"
            >

                {text}

            </div>

            {
                !isUser && confidence !== undefined && (

                    <div className="ml-13 mt-5">

                        <span
                            className={`inline-block px-4 py-2 rounded-full text-sm font-semibold

                            ${
                                confidence >= 60

                                    ? "bg-green-100 text-green-700"

                                : confidence >= 20

                                    ? "bg-yellow-100 text-yellow-700"

                                : "bg-red-100 text-red-700"
                            }`}
                        >

                            {
                                confidence >= 60

                                    ? "🟢 High Retrieval Match"

                                : confidence >= 20

                                    ? "🟡 Medium Retrieval Match"

                                : "🔴 Low Retrieval Match"
                            }

                            {" • "}

                            {confidence.toFixed(1)}%

                        </span>

                    </div>

                )
            }

        </div>

    );

}

export default Message;