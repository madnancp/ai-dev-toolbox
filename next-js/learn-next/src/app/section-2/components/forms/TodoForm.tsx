import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { RadioGroup } from "@/components/ui/radio-group";
import { Textarea } from "@/components/ui/textarea";
import { TaskPriority, Task } from "@/types/shared";
import { RadioGroupItem } from "@/components/ui/radio-group";
import { useState } from "react";

type Prop = {
  onAdd: (newTask: Task) => void;
}

const TodoForm = ({ onAdd }: Prop) => {
  const [id, setId] = useState<number>(0);
  const [name, setName] = useState<string>("")
  const [descreption, setDescreption] = useState<string>("")
  const [priority, setPriority] = useState<string>(TaskPriority.Medium)

  const handleFormSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (name != "" && descreption != "" && priority) {
      const newTask: Task = {
        id: id,
        name: name,
        descreption: descreption,
        priority: priority
      }
      onAdd(newTask)
      setId(id => id + 1);
    }
  }

  return (
    <form className="flex justify-center items-center gap-2 flex-col" onSubmit={handleFormSubmit}>
      <h1 className="text-lg font-bold">Add New Task!</h1>
      <div>
        <Input
          placeholder="Task"
          type="text"
          value={name}
          onChange={(e) => { setName(e.target.value) }}
        />
      </div>

      <div>
        <Textarea
          placeholder="Descreption"
          value={descreption}
          onChange={(e) => { setDescreption(e.target.value) }}
        />
      </div>

      <Label className="text-gray-400">Priority</Label>
      <RadioGroup defaultValue={TaskPriority.Medium} className="flex" onValueChange={(value) => setPriority(value)}>
        <div className="flex items-center gap-1">
          <RadioGroupItem value={TaskPriority.Low} id="p1" />
          <Label htmlFor="p1">Low</Label>
        </div>

        <div className="flex items-center gap-1">
          <RadioGroupItem value={TaskPriority.Medium} id="p2" />
          <Label htmlFor="p2">Medium</Label>
        </div>

        <div className="flex items-center gap-1">
          <RadioGroupItem value={TaskPriority.High} id="p3" />
          <Label htmlFor="p3">High</Label>
        </div>
      </RadioGroup>

      <div>
        <Button
          variant="default"
          size="sm">
          Add Task
        </Button>
      </div>
    </form >
  )
}

export default TodoForm;
