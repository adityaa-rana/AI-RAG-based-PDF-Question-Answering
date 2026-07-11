function Loader() {

    return (

        <div className="flex items-center gap-2 ml-13 mt-4">

            <span className="w-3 h-3 rounded-full bg-blue-500 animate-bounce"></span>

            <span
                className="w-3 h-3 rounded-full bg-blue-500 animate-bounce"
                style={{ animationDelay: "0.15s" }}
            ></span>

            <span
                className="w-3 h-3 rounded-full bg-blue-500 animate-bounce"
                style={{ animationDelay: "0.3s" }}
            ></span>

        </div>

    );

}

export default Loader;