import { useState } from "react";
import { Button } from "../ui/button";
import { CircleCheck, CircleX } from "lucide-react";

type Props = {
	name: string,
	descreption: string,
	priority: string,
}

const TaskCard = (props: Props) => {
	const [isCompleted, setIsCompleted] = useState<boolean>(false)
	return (
		<div className={`flex justify-between items-center min-w-50 max-w-96 border p-5 rounded-lg ${isCompleted && 'opacity-40 line-through'} ${props.priority === 'high'
			? 'bg-red-600/10 border-red-300'
			: props.priority === "medium"
				? 'bg-yellow-600/10 border-yellow-300'
				: 'bg-gray-200/10 border-white'
			}`} >
			<div>
				<h1 className="text-lg font-bold">{props.name}</h1>
				<p className="text-md text-gray-400">{props.descreption}</p>
				<p className="text-md">Priority:
					<span className={`${props.priority == 'high'
						? 'text-red-600'
						: props.priority == 'medium'
							? 'text-yellow-600'
							: 'text-yellow-100'
						} font-semibold`}> {props.priority}</span></p>
			</div>
			<div>
				<Button variant="outline" size="icon" onClick={() => { setIsCompleted(!isCompleted) }}>
					{!isCompleted
						? <CircleCheck />
						: <CircleX />
					}
				</Button>
			</div>
		</div >
	)
}

export default TaskCard;
