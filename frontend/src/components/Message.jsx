function Message({ role, text }) {

    const isUser = role === "user";

    return (

        <div className="mb-8">

            <div className="flex items-center gap-3 mb-3">

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

            <div
                className="ml-13 text-lg leading-8 text-slate-700 whitespace-pre-wrap"
            >
                {text}
            </div>

        </div>

    );

}

export default Message;