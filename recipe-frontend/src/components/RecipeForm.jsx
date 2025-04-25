import { useState } from 'react'
import { Form, Input, Button, Select, message } from 'antd'
import axios from 'axios'

const RecipeForm = ({ onRecipeGenerated }) => {
  const [form] = Form.useForm()
  const [loading, setLoading] = useState(false)

  const onFinish = async (values) => {
    try {
      setLoading(true)
      const response = await axios.post('http://localhost:8000/recipes/generate', {
        ingredients: values.ingredients.split(',').map(i => i.trim()),
        diet: values.diet,
        cuisine: values.cuisine
      })
      onRecipeGenerated(response.data)
    } catch (error) {
      message.error('Ошибка при генерации рецепта')
      console.error(error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <Form form={form} onFinish={onFinish} layout="vertical">
      <Form.Item
        name="ingredients"
        label="Ингредиенты (через запятую)"
        rules={[{ required: true, message: 'Введите хотя бы один ингредиент' }]}
      >
        <Input placeholder="яйца, молоко, мука" />
      </Form.Item>

      <Form.Item name="diet" label="Диета">
        <Select placeholder="Выберите диету">
          <Select.Option value="обычная">Обычная</Select.Option>
          <Select.Option value="веганская">Веганская</Select.Option>
          <Select.Option value="безглютеновая">Без глютена</Select.Option>
        </Select>
      </Form.Item>

      <Form.Item name="cuisine" label="Кухня">
        <Select placeholder="Выберите кухню">
          <Select.Option value="русская">Русская</Select.Option>
          <Select.Option value="итальянская">Итальянская</Select.Option>
          <Select.Option value="азиатская">Азиатская</Select.Option>
        </Select>
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit" loading={loading}>
          Сгенерировать рецепт
        </Button>
      </Form.Item>
    </Form>
  )
}

export default RecipeForm