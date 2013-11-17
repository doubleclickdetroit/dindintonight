<?php
/**
 * @Entity @Table(name="dropmeals")
 */
class DropMeal
{
    /**
     * @Id @GeneratedValue @Column(type="integer")
     * @var int
     */
    protected $id;

    /**
     * @Column(type="integer")
     * @var integer
     */
    protected $drop_id;

    /**
     * @Column(type="integer")
     * @var integer
     */
    protected $meal_id;

    /**
     * @Column(type="integer")
     * @var integer
     */
    protected $quantity;

    public function getId()
    {
        return $this->id;
    }

    public function getDropId()
    {
        return $this->drop_id;
    }

    public function setDropId($drop_id)
    {
        $this->drop_id = $drop_id;
    }

    public function getMealId()
    {
        return $this->meal_id;
    }

    public function setMealId($meal_id)
    {
        $this->meal_id = $meal_id;
    }

    public function getQuantity()
    {
        return $this->quantity;
    }

    public function setQuantity($quantity)
    {
        $this->quantity = $quantity;
    }

}
