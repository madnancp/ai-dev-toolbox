import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { TaskCrud } from "@/services/task.service";
import { TaskPriority } from "@/types/shared";
import { useState } from "react";

type Prop = {
  onEdit: () => void;
  id: string,
  name: string,
  description?: string,
  priority: TaskPriority,
}

const EditTaskFrom = (props: Prop) => {

  const [taskName, setTaskName] = useState<string>(props.name);
  const [taskDesc, setTaskDesc] = useState<string>(props.description);
  const [taskPriority, setTaskPriority] = useState<TaskPriority>(props.priority);
  const [taskNameError, setTaskNameError] = useState<string | null>(null)

  const handleEditTaskFormSubmission = async (e: React.FormEvent) => {
    e.preventDefault()
    if (taskName === "") {
      setTaskNameError("please enter a task name")
      return
    }

    const result = await TaskCrud.updateTask(
      { id: props.id, name: taskName, description: taskDesc, priority: taskPriority }
    )
    console.log(result)

    props.onEdit()

    console.log({
      name: taskName,
      description: taskDesc,
      priority: taskPriority
    })
  }

  return (
    <form onSubmit={handleEditTaskFormSubmission} className="flex flex-col gap-2">
      <div>
        <Label className="text-sm text-gray-300" htmlFor="editTaskName">Name</Label>
        <Input type="text" value={taskName} onChange={(e) => { setTaskName(e.target.value) }} id="editTaskName" />
        {taskNameError && (
          <span className="text-red-500 text-sm">{taskNameError}</span>
        )}
      </div>

      <div>

        <Label className="text-sm text-gray-300" htmlFor="editTaskDesc">Description</Label>
        <Input type="text" value={taskDesc} onChange={(e) => { setTaskDesc(e.target.value) }} id="editTaskDesc" />
      </div>

      <Label className="text-sm text-gray-300">Priority</Label>
      <RadioGroup value={taskPriority} className="flex justify-evenly mb-3" onValueChange={(value: TaskPriority) => setTaskPriority(value)}>
        <div className="flex justify-center items-center gap-2">
          <RadioGroupItem value={TaskPriority.Low} id="pedit1" />
          <Label htmlFor="pedit1">Low</Label>
        </div>

        <div className="flex justify-center items-center gap-2">
          <RadioGroupItem value={TaskPriority.Medium} id="pedit2" />
          <Label htmlFor="pedit2">Medium</Label>
        </div>

        <div className="flex justify-center items-center gap-2">
          <RadioGroupItem value={TaskPriority.High} id="pedit3" />
          <Label htmlFor="pedit3">High</Label>
        </div>
      </RadioGroup>
      <Button>Save</Button>
    </form >
  )
}

export default EditTaskFrom;
