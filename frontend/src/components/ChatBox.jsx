import { useEffect, useRef } from "react";

import Message from "./Message";
import Loader from "./Loader";

function ChatBox({ messages, loading }) {

    const bottomRef = useRef(null);

    useEffect(() => {

        bottomRef.current?.scrollIntoView({
            behavior: "smooth"
        });

    }, [messages, loading]);

    return (

        <section
            className="bg-white rounded-2xl shadow-lg border border-slate-200 p-10 mb-8 h-[500px] overflow-y-auto"
        >

            {
                messages.length === 0 ? (

                    <div className="flex flex-col items-center justify-center h-full text-center">

                        <div className="text-6xl mb-5">
                            💬
                        </div>

                        <h2 className="text-3xl font-bold text-slate-800">

                            Upload a PDF to begin

                        </h2>

                        <p className="mt-3 text-lg text-slate-500">

                            Ask questions about your document using AI.

                        </p>

                    </div>

                ) : (

                    <>
                        {
                            messages.map((message, index) => (

                                <Message
                                    key={index}
                                    role={message.role}
                                    text={message.text}
                                />

                            ))
                        }

                        {
                            loading &&
                            <Loader />
                        }

                        <div ref={bottomRef} />

                    </>

                )

            }

        </section>

    );

}

export default ChatBox;