<?php
/**
 * @Entity @Table(name="payments")
 */
class Payment
{
    /**
     * @Id @GeneratedValue @Column(type="integer")
     * @var int
     */
    protected $id;

    /**
     * @Column(type="integer")
     * @var string
     */
    protected $user_id;

    /**
     * @Column(type="integer")
     * @var string
     */
    protected $location_id;

    public function getId()
    {
        return $this->id;
    }

    public function getUserId()
    {
        return $this->user_id;
    }

    public function setUserId($user_id)
    {
        $this->user_id = $user_id;
    }

    public function getLocationId()
    {
        return $this->location_id;
    }

    public function setLocationId($location_id)
    {
        $this->location_id = $location_id;
    }

}
