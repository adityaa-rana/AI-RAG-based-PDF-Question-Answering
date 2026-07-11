import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";


export async function askQuestion(question) {

    const response = await axios.post(

        `${BASE_URL}/ask`,

        {
            question: question
        }

    );

    return response.data;

}