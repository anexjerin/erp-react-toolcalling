import { useEffect, useRef, useState } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
// import { useFrappeAuth } from 'frappe-react-sdk';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { toolsCalling } from '../../api/toolsCalling';


interface Message {
  message: string;
}

interface Response {
  role: string;
  text: string;
}

export const Chatbox = () => {
  // const { currentUser } = useFrappeAuth();
  const { register, handleSubmit, reset } = useForm<Message>();
  const chatContainerRef = useRef<HTMLDivElement>(null);
  const [messages, setMessagges] = useState<Response[]>([]);
  // const { currentUser, logout } = useFrappeAuth();

  // const [loading, setLoading] = useState<boolean>(false);
  const sendMessage: SubmitHandler<Message> = (data) => {
    // const userId = currentUser;
    // console.log(data.message);

    setMessagges((prevmsg) => [
      ...prevmsg,
      { role: 'human', text: data.message },
    ]);

    const messageFromBot = async (message: string) => {
      const botMessage = await toolsCalling(message);
      let botMessageStr = '';
      if (Array.isArray(botMessage)) {
        botMessageStr = botMessage
          .map((item) => {
            if (typeof item === 'string') {
              return item; // If it's a string, just return the string
            } else if (Array.isArray(item)) {
              return item.join('\n');
            } else if (typeof item === 'object' && item !== null) {
              // If it's an object, map through the key-value pairs
              return Object.entries(item)
                .map(([key, value]) => `${key}: ${value}`)
                .join(', ');
            } else {
              return 'Unknown data type'; // In case of an unexpected element
            }
          })
          .join('\n ');
      } else if (typeof botMessage === 'object' && botMessage !== null) {
        botMessageStr = Object.entries(botMessage)
          .map(([key, value]) => `${key}: ${value}`)
          .join(', ');
      } else botMessageStr = botMessage as string;

      setMessagges((prevmsg) => [
        ...prevmsg,
        { role: 'bot', text: botMessageStr },
      ]);
    };
    messageFromBot(data.message);
    reset();
    // return res;
  };
  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop =
        chatContainerRef.current.scrollHeight;
    }
  }, [messages]);
  return (
    <div className='w-full flex justify-center items-center flex-col gap-5 '>
      <div className='flex flex-col justify-between gap-5 bg-white p-3 rounded-xl w-[50%] h-[70%] relative shadow-sm '>
        <div className='flex flex-col gap-3'>
          <div
            ref={chatContainerRef}
            className='px-3 py-3 font-nunito flex flex-col gap-3 overflow-y-auto max-h-[500px] scroll-smooth '
          >
            {messages.map((message, index) => (
              <p
                key={index}
                className={`${message.role} max-w-[90%] w-fit py-2 px-5 rounded-xl whitespace-pre-line text-[18px] `}
                // className='bg-mine-subtle_bg w-fit py-2 px-3 rounded-sm break-words text-wrap break-all text-[18px] '
              >
                {message.text}
              </p>
            ))}
          </div>
        </div>
        <form
          onSubmit={handleSubmit(sendMessage)}
          autoComplete='off'
          className='relative bottom-0 left-0 w-full flex p-3 gap-2  border-t rounded-md '
        >
          <Input
            className='bg-white w-full '
            placeholder='Type your message here'
            {...register('message', { required: true })}
          />
          <Button
            className='w-full max-w-[100px]  p-3 cursor-pointer'
            type='submit'
          >
            Send
          </Button>
        </form>
      </div>
    </div>
  );
};


