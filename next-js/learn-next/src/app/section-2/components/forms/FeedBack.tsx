import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { useState } from "react";

const FeedBackForm = () => {
  const [name, setName] = useState<string>("")
  const [message, setMessage] = useState<string>("")


  const handleFormSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (name != "" && message != "") {
      alert(`name : ${name}\nmessage: ${message}`)
    }
  }

  return (
    <form className="flex justify-center items-center gap-2 flex-col border rounded-3xl shadow" onSubmit={handleFormSubmit}>
      <h1 className="text-lg font-bold">Drop Your Feedback!</h1>
      <div>
        <Input
          placeholder="name"
          type="text"
          value={name}
          onChange={(e) => { setName(e.target.value) }}
        />
      </div>

      <div>
        <Textarea
          placeholder="Type your message here."
          value={message}
          onChange={(e) => { setMessage(e.target.value) }}
        />
      </div>

      <div>
        <Button
          variant="default"
          size="sm">
          Submit
        </Button>
      </div>
    </form >
  )
}

export default FeedBackForm;
