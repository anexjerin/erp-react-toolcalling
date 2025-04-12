import axios from 'axios';

export const toolsCalling = async (
  message: string
): Promise<object | string> => {
  try {
    const csrfToken = (window as any)?.csrf_token;
    console.log(csrfToken)
    const res = await axios.post(
      '/api/method/doodle.chat_app.app.chat_bot',
      { data: message },
      {
        withCredentials: true,
        headers: {
          'X-Frappe-CSRF-Token': csrfToken,
          'Content-Type': 'application/json',
        },
      }
    );

    if (res.data && res.data.message) {
      console.log(res.data.message);
      return res.data.message;
    } else {
      throw new Error('No message found in the response');
    }
  } catch (error: any) {
    console.error('Error calling the function:', error);

    // Return a user-friendly error message
    return `Error occurred: ${error.message || 'Unknown error'}`;
  }
};
